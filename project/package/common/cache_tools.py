import functools
from datetime import datetime
import shutil

from package.constants import CACHE_DIR


def serialized_cache(salt: str, maxsize: int = 64):

    def _serialized_cache(func):

        n_cachefiles = len(list(CACHE_DIR.iterdir())) if CACHE_DIR.exists() else 0
        if n_cachefiles > maxsize:
            shutil.rmtree(CACHE_DIR)

        if not CACHE_DIR.exists():
            CACHE_DIR.mkdir()

        def wrapper(*args, **kwargs):
            import pdb; pdb.set_trace()
            return func(*args, **kwargs)

        return wrapper

    return _serialized_cache


daily_cache = functools.partial(serialized_cache, salt=datetime.now().strftime("DAY%Y%m%d"))()

weekly_cache = functools.partial(serialized_cache, salt=datetime.now().strftime("WEEK%Y%W"))()

monthly_cache = functools.partial(serialized_cache, salt=datetime.now().strftime("MONTH%Y%M"))()



if __name__ == '__main__':

    import pandas as pd
    from sklearn.datasets import load_iris

    @daily_cache
    def load_dataset(alpha, beta=3.2):
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        return df

    df = load_dataset(2.1, 3.2)
    df = load_dataset(alpha=2.1, beta=3.2)
    df = load_dataset(beta=2.1, alpha=3.2)
