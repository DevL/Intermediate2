# Exercise 04 - Type hints

We will be adding type hints to our `Recallculator` class. As we do, examine how your editor, e.g. VS Code, treats calls and references to methods and attributes when you hover your mouse cursor over them. You can also run `mypy` to check the type hints, though be aware that that tool does not treat all type hints exactly the same as the Python documentation describes. From this directory in the terminal, run `mypy recallculator` to type check the `recallculator` package.

1. Add a type hint to `add`.
    * Keep in mind that while we might not have tested it before, we have no real reason to disallow the addition of two `float` or a `float` and an `int`. 
        * One way is to create a type alias using `Union`.
        * Another solution is hidden in [PEP 484](https://peps.python.org/pep-0484/#the-numeric-tower).
    * Remember to type hint both the parameters and the return value.
    * Ignore type hinting `self` for now.
2. Add similar type hints to `subtract`, `multiply`, and `divide`.
    * Carefully consider the return type of `divide` compared to the other methods. If in doubt, use the Python REPL to explore how division behaves.
3. Type hint `__repr__`.
    * The return value should be straight forward, but if not, take a look at the implementation of `__repr__` and the documentation for [`object.__repr__`](https://docs.python.org/3.9/reference/datamodel.html#object.__repr__).
4. Type hint the `operations` property.
    * Note that a list of strings allow the list to be empty. 

## Bonus round (optional)

How do you type hint `self`?
* Typically you don't. Unless you have a method returning an instance of the class.
* If you do, it depends on your version of Python.
    * In Python 3.11+ you can use `from typing import Self` and use `Self` as the type.
    * In older versions you can use `from typing_extensions import Self`.

5. Add method to `Recallculator` called `inspect` that takes no parameters other than `self`, prints the contents of the `operations` list, and then returns the instance.
    * Type hint the return value accordingly.
    * You can test the new method by running a REPL from this directory, importing the package, creating an instance, and then sending it the `inspect` message. Notice the output in the REPL.
    * To TDD this method, you need to know how to capture and access the stdout output with pytest. You can use the [`capsys fixture`](
    https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html) to do this.    


6. Why should you not annotate the return type of `__init__`, and if you do, what should the return type be?
    * The answer is in [PEP 484](https://peps.python.org/pep-0484/#the-meaning-of-annotations).

## Additional notes

Tests have been provided. Run them by entering into this directory in the terminal and run `pytest`. It is expected that they all pass.

## Solution notes

Tests have been provided. Run them by entering into the _solutions/04_type_hints_ directory in the terminal and run `pytest`.
