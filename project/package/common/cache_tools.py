from typing import Literal
import functools
from datetime import datetime


def serialized_cache(term=Literal["daily", "weekly", "monthly"]):

    if term == "daily":
        salt = datetime.now().strftime("DAY%Y%m%d")
    elif term == "weekly":
        salt = datetime.now().strftime("WEEK%Y%W")
    elif term == "monthly":
        salt = datetime.now().strftime("MONTH%Y%M")
    else:
        raise ValueError(f"Invalid term: {term}")

    def _serialized_cache(func):

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return _serialized_cache


daily_cache = functools.partial(serialized_cache, term="daily")
weekly_cache = functools.partial(serialized_cache, term="weekly")
monthly_cache = functools.partial(serialized_cache, term="monthly")
