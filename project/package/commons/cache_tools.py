import pandas as pd


def serialized_lru_cache(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def weekly_cache(func):
    week_idx = "2207"
    funcname = func.__name__
    pass
