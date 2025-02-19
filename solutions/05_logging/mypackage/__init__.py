from .my_module import first


def hello():
    return "Hello, I'm in a package."


__all__ = ["first", "hello"]
