def say_spam(n: int):
    """sample function

    Args:
        n (int): _description_

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    if type(n) != int:
        raise TypeError(f"n must be int: given {n}")
    return "spam" * 3
