import functools

from functools import lru_cache


@lru_cache(None)
def func(x, y):
    """This is a docstring"""
    if x < 0:
        raise ValueError()
    return x + 2.0 * y


class A:
    def __init__(self, x, y):
        self.x = x  # This is a useless comment
        self.y = y

    def say_hello(self):
        print(f"Hello, world\nx = {self.x}\ny = {self.y}")


if __name__ == "__main__":
    a = A(1.0, 2.0)
    a.say_hello()
