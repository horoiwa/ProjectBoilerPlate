import functools
import hashlib
import pickle
import shutil
from datetime import datetime

from package.constants import CACHE_DIR


def serialized_cache(salt: str, maxsize: int = 64):
    def _serialized_cache(func):

        n_cachefiles = len(list(CACHE_DIR.iterdir())) if CACHE_DIR.exists() else 0
        if n_cachefiles > maxsize:
            shutil.rmtree(CACHE_DIR)

        if not CACHE_DIR.exists():
            CACHE_DIR.mkdir()

        def wrapper(*args, **kwargs):

            # saltか引数が異なれば異なるmessage_digestになる
            argslist = [str(v) for v in args] + [str(v) for v in kwargs.values()]
            message = salt + "_" + func.__name__ + "_".join(argslist)
            message_digest = hashlib.sha256(message.encode()).hexdigest()

            match = list(CACHE_DIR.glob(f"{message_digest}.*"))
            if match:
                # キャッシュに存在する場合はロードする
                # dataframeはparquet, それ以外はpickle
                filepath = match[0]
                if filepath.suffix == ".parquet":
                    data = pd.read_parquet(CACHE_DIR / f"{message_digest}.parquet")
                else:
                    with open(CACHE_DIR / f"{message_digest}.pkl", "rb") as f:
                        data = pickle.load(f)
            else:
                # キャッシュに存在しない場合は、func実行後に保存
                # dataframeはparquet, それ以外はpickle
                data = func(*args, **kwargs)
                if isinstance(data, pd.DataFrame):
                    data.to_parquet(CACHE_DIR / f"{message_digest}.parquet")
                else:
                    with open(CACHE_DIR / f"{message_digest}.pkl", "wb") as f:
                        pickle.dump(data, f)

            return data

        return wrapper

    return _serialized_cache


daily_cache = functools.partial(
    serialized_cache, salt=datetime.now().strftime("DAY%Y%m%d"))()

weekly_cache = functools.partial(
    serialized_cache, salt=datetime.now().strftime("WEEK%Y%W"))()

monthly_cache = functools.partial(
    serialized_cache, salt=datetime.now().strftime("MONTH%Y%M"))()


if __name__ == "__main__":

    import time

    import pandas as pd
    from sklearn.datasets import load_iris

    @daily_cache
    def load_dataset(alpha, beta=3.2):
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        time.sleep(5)
        return df

    @daily_cache
    def load_dict(alpha, beta):
        time.sleep(5)
        return {"a": alpha, "b": beta}

    df = load_dataset(2.1, 3.2)
    print(df)
    df = load_dataset(alpha=2.1, beta=3.2)
    print(df)
    df = load_dataset(beta=2.1, alpha=3.2)
    print(df)

    d = load_dict(2.1, 3.2)
    print(d)
    d = load_dict(alpha=2.1, beta=3.2)
    print(d)
    d = load_dict(beta=2.1, alpha=3.2)
    print(d)

    d = load_dict(beta={"a": 2}, alpha=3.2)
