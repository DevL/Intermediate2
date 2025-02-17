from .my_module import first


def hello():
    return "Hello, I'm in a package."


this_is_public = 1
_this_is_private = 2

__all__ = ["first", "hello"]
