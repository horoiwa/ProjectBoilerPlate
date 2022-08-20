from typing import Literal
import functools
from datetime import datetime


def serialized_cache(period=Literal["daily", "weekly", "monthly"]):

    if period == "daily":
        salt = datetime.now().strftime("DAY%Y%m%d")
    elif period == "weekly":
        salt = datetime.now().strftime("WEEK%Y%W")
    elif period == "monthly":
        salt = datetime.now().strftime("MONTH%Y%M")
    else:
        raise ValueError(f"Invalid term: {period}")

    print(salt)

    def _serialized_cache(func):

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return _serialized_cache


daily_cache = functools.partial(serialized_cache, term="daily")
weekly_cache = functools.partial(serialized_cache, term="weekly")
monthly_cache = functools.partial(serialized_cache, term="monthly")
