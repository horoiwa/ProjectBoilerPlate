import pytest

from package.module1.api import say_spam


def test_say_hello():

    assert say_spam(n=3) == "spam"*3

    with pytest.raises(TypeError):
        say_spam(n="3")
