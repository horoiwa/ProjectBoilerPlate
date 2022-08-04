

def serialized_lru_cache(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def weekly_cache(func):
    pass
