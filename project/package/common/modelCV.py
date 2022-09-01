from abc import ABC, abstractmethod, abstractproperty
from typing import Callable, Literal, Optional

import optuna
import pandas as pd
from lightgbm import LGBMClassifier, LGBMRegressor
from sklearn.linear_model import Ridge
from sklearn.model_selection import RepeatedKFold
from sklearn.svm import SVC, SVR

from package.constants import logger


class BaseModelCV(ABC):
    def __init__(
        self,
        n_splits: int = 3,
        n_repeats: int = 1,
        metric_func: Optional[Callable] = None,
        direction: Literal["minimize", "maximize"] = "maximize",
    ):
        """sklearn.linear_model.RidgeCV のTPE版

        Args:
            n_folds (int, optional):
                train_valid_split時のK_FOLDの切り数. Defaults to 3.
            n_repeat (int, optional):
                k_foldを何回繰り返すか. Defaults to 1.
            metric_func (Optional[Callable], optional):
                ハイパラチューニング時のメトリック関数 (sklearn.metrics.*)
                Noneの場合はmodel.scoreを使用 Defaults to None.
            direction (str):
                metricを最大化するか最小化するか Defaults to "maximize"
        """
        self.model = None
        self.n_splits = n_splits
        self.n_repeats = n_repeats
        self.metric_func = metric_func
        self.direction = direction

    def __getattr__(self, attr: str):
        return getattr(self.model, attr)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__.update(d)

    @abstractproperty
    def model_class(self):
        raise NotImplementedError()

    @abstractmethod
    def define_search_space(self, trial):
        raise NotImplementedError()

    def fit(self, X: pd.DataFrame, Y: pd.Series, n_trials: int = 150):

        assert isinstance(X, pd.DataFrame)
        assert isinstance(Y, (pd.DataFrame, pd.core.series.Series))
        assert X.shape[0] == Y.shape[0]
        assert Y.shape[1] == 1

        if n_trials == 0:
            #: Use default parameter
            best_params = {}
        else:
            #: Run hyper params optimization
            best_trial, best_params = self._param_search(X, Y, n_trials)
            logger.info("==== Best Trial =====")
            logger.info(best_trial)
            logger.info("==== Best Params =====")
            logger.info(best_params)

        self.model = self.model_class(**best_params)
        self.model.fit(X, Y)

    def _param_search(self, X: pd.DataFrame, Y: pd.Series, n_trials: int):
        def objective(trial):
            params = self.define_search_space(trial)
            model = self.model_class(**params)
            kf = RepeatedKFold(n_splits=self.n_splits, n_repeats=self.n_repeats)
            split_gen = kf.split(X)

            scores = []
            for train_index, test_index in split_gen:
                X_train, X_test = X.iloc[train_index, :], X.iloc[test_index, :]
                Y_train, Y_test = Y.iloc[train_index], Y.iloc[test_index]
                model.fit(X_train, Y_train)
                if self.metric_func is None:
                    score = model.score(X_test, Y_test)
                else:
                    Y_test_pred = model.predict(X_test)
                    score = self.metric_func(Y_test.values.flatten(), Y_test_pred)
                scores.append(score)

            avg_score = sum(scores) / len(scores)
            return avg_score

        study = optuna.create_study(direction=self.direction)
        study.optimize(objective, n_trials=n_trials)

        return study.best_trial, study.best_trial.params


class RidgeCV(BaseModelCV):
    @property
    def model_class(self):
        return Ridge

    def define_search_space(self, trial):
        params = {
            "alpha": trial.suggest_loguniform("alpha", 1e-3, 1e2),
        }
        return params


class SVRCV(BaseModelCV):
    @property
    def model_class(self):
        return SVR

    def define_search_space(self, trial):
        params = {
            "kernel": "rbf",
            "C": trial.suggest_loguniform("C", 1e-2, 1e2),
            "epsilon": trial.suggest_loguniform("epsilon", 1e-3, 1e2),
            "gamma": trial.suggest_loguniform("gamma", 1e-3, 1e3),
        }

        return params


class LGBRCV(BaseModelCV):
    @property
    def model_class(self):
        return LGBMRegressor

    def define_search_space(self, trial):
        params = {
            "num_leaves": trial.suggest_int("num_leaves", 2, 256),
            "subsample": trial.suggest_uniform("subsample", 0.5, 1.0),
            "max_depth": trial.suggest_int("max_depth", 1, 8),
            "min_child_samples": trial.suggest_int("min_child_samples", 8, 128),
            "extra_trees": True,
            "reg_alpha": trial.suggest_loguniform("reg_alpha", 1e-8, 10.0),
            "reg_lambda": trial.suggest_loguniform("reg_lambda", 1e-8, 10.0),
        }
        return params


class SVCCV(BaseModelCV):
    @property
    def model_class(self):
        raise SVC

    def define_search_space(self, trial):
        params = {
            "kernel": "rbf",
            "C": trial.suggest_loguniform("C", 1e-2, 1e2),
            "gamma": trial.suggest_loguniform("gamma", 1e-3, 1e3),
        }
        return params


class LGBCV(BaseModelCV):
    @property
    def model_class(self):
        return LGBMClassifier

    def define_search_space(self, trial):
        params = {
            "num_leaves": trial.suggest_int("num_leaves", 2, 256),
            "subsample": trial.suggest_uniform("subsample", 0.5, 1.0),
            "max_depth": trial.suggest_int("max_depth", 1, 8),
            "min_child_samples": trial.suggest_int("min_child_samples", 8, 128),
            "extra_trees": True,
            "reg_alpha": trial.suggest_loguniform("reg_alpha", 1e-8, 10.0),
            "reg_lambda": trial.suggest_loguniform("reg_lambda", 1e-8, 10.0),
        }
        return params


if __name__ == "__main__":
    from sklearn.datasets import load_boston

    bos = load_boston()
    X = pd.DataFrame(bos.data, columns=bos.feature_names)
    Y = pd.DataFrame(bos.target, columns=["Price"])
    model = SVRCV()
    model.fit(X, Y, n_trials=100)
