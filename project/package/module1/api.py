

def say_spam(n: int):
    if type(n) != int:
        raise TypeError(f"n must be int: given {n}")
    return "spam"*3
