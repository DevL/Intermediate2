# Documentation and Doctests

A primary means of documenting Python code is to add so called [docstrings](https://peps.python.org/pep-0257/#what-is-a-docstring) to packages, modules, classes, methods, and functions. Once added, the documentation is available in the REPL by issuing `help(something_that_has_been_documented)`. 

## Doctests

Documentation is practically comments and as any seasoned developer knows, comments tend to be forgotten as the code changes. At best they're harmlessly out of data, at worst they're misleading.

But what if we could execute the documentation as part of running our tests? Enter doctests. 

In addition to containg plain documentation, docstrings can be turned into executable tests called [doctests](https://docs.pytest.org/en/stable/how-to/doctest.html). A common way to make pytest run doctests is `pytest --doctest-modules --doctest-continue-on-failure`. One can also configure this as default options in e.g. a `pyproject.toml` file as has been done in this repository.

The format of a doctest is intended to look like lines where being entered into a Python REPL and the results returned. For example, to test thast the built-in `str` function correctly converts a number to a string, one could imagine the following doctest being added to the docstring of `str`.

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

Notice that a quirk of doctests is that strings are output using single quotes. Expecting string in double quotes will result in ab assertion error.

## Exercise 03

See _exercises/03_docs/instructions.md_.
