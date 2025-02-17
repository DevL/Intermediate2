# Type hints

Python is a dynamically typed language and while it simply cannot give the same runtime guarantees that a statically language can give. There are other benefits to being a dynamically typed language, but those are outside the scope of this course.

With that said, one can introduce type hints as a form of documentation and to aid certain tools such code editors, type checkers, and linters.

## Examples

### A basic example

Given a simple function that takes a name and returns a greeting, we could type hint its parameter and its return value like this:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

* Note that `str` refers to the built-in type [`str`]().

### A compound example

```python
from typing import NewType

class Username(str):
    ...

class Email(str):
    ...

UserKey = Union[Username, Email]

def lookup_user(username_or_email: UserKey) -> Optional[User]:
    ...
```

In this example, the function `lookup_user` will accept either an instance of `Username` or an instance of `Email` as its parameter and return a `User` instance if it can find one or `None` if it cannot.

* Both `Username` and `Email` are subclasses of `str`. While they're both strings, they conceptually represent different things. Subclasses can be a good way of showing this in the code base.
* `UserKey` is a [type alias](https://peps.python.org/pep-0484/#type-aliases). We can use type aliases to avoid repetion or to name concepts such as what a union of a couple of types mean to us.
* Note that `Optional[User]` is shorthand for `Union[User, None]`.
* For brevity, the `User` class is not part of the example.

## Resources

* The [`typing`](https://docs.python.org/3.9/library/typing.html#module-typing) module provides support for adding type hints that are more complex than just specifying a simple class.
* MyPy provides a [cheatsheet for type hints](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).
* There is a package called [`typing-extensions`](https://pypi.org/project/typing-extensions) that provides backports of new type hinting support for older Python versions.

## A note on Python versions

The availability of and support for type hints vary quite a bit between versions of Python. For example, [`NewType`](https://docs.python.org/3.13/library/typing.html#newtype) is a function up to Python 3.9, but a class from Python 3.10 and [`typing.callable`](https://docs.python.org/3.13/library/typing.html#typing.Callable) was deprecated in 3.9 in favour of [`collections.abc.callable`](https://docs.python.org/3.13/library/collections.abc.html#collections.abc.Callable) and so on and so forth.

The exercises in this repository are set up for Python 3.9 with the `typing-extensions` package installed, but if you are using something else, make sure that you read and use the documentation and syntax for your version of Python.

## Exercise 04

See _exercises/04_type_hints/instructions.md_.
