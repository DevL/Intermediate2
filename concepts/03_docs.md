# Documentation and Doctests

A primary means of documenting Python code is to add so called [docstrings](https://peps.python.org/pep-0257/#what-is-a-docstring) to packages, modules, classes, methods, and functions. Once added, the documentation is available in the REPL by issuing `help(something_that_has_been_documented)`.

An example of a docstring added to a function follows.

```python
def greeting(name):
    """
    Returns a greeting to the name provided.
    """
    return f"Hello, {name}" 
```

## Doctests

Documentation is practically comments and as any seasoned developer knows, comments tend to be forgotten as the code changes. At best they're harmlessly out of data, at worst they're misleading.

But what if we could execute the documentation as part of running our tests? Enter [doctests](https://docs.python.org/3/library/doctest.html).

In addition to containing plain documentation, docstrings can include executable examples called doctests.

The format of a doctest is intended to look like lines where being entered into a Python REPL and the results returned. For example, to test that the built-in `str` function correctly converts a number to a string, one could imagine the following doctest being added to the docstring of `str`.

```python
"""
...the existing documentation for str.

>>> str(1)
'1'
"""
```

A full example of a documented function with a doctest follows.

```python
def greeting(name):
    """
    Returns a greeting to the name provided.

    >>> greeting("Lennart")
    'Hello, Lennart'
    """
    return f"Hello, {name}"
```

Notice that a quirk of doctests is that strings are output using single quotes. Expecting string in double quotes will result in an assertion error.

### Running doctests with pytest

A common way to make pytest run doctests is `pytest --doctest-modules --doctest-continue-on-failure`. One can also configure this as default options in e.g. a `pyproject.toml` file as has been done in this repository. For full details see [the pytest documentation](https://docs.pytest.org/en/stable/how-to/doctest.html).

## Exercise 03

See _exercises/03_docs/instructions.md_.

## Additional notes

If you think executable documentation sounds like a neat concept in general, you should take a closer look at Donald Knuth's [_Literate Programming_](https://en.wikipedia.org/wiki/Literate_programming).
