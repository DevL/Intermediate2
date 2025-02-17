# Exercise 03 - Documentation and Doctests

An implementation of our old friend `Recallculator` has been provided, together with a set of tests.

The goal of this exercise is to reimplement some of the tests as doctests while also documenting the public API of the `Recallculator` class.

## Documenting the methods

1. Run the tests.
    * Notice that five tests are failing as the methods `add`, `subtract`, `multiply`, `divide`, and `operations` haven't been documented.
    * Notice that we're _accessing_ the method objects, not sending a message to an instance. That's why we access them via the class rather than through an instance, though we could also do the latter.
    * Notice that methods (just like functions and classes) are objects and they have their own set of attributes. One of those attributes is `__doc__` that contains a [docstring](https://peps.python.org/pep-0257/#what-is-a-docstring). In our case, we haven't specified any docstring so `__doc__` will be `None`.
2. Starting with `add`, add a docstring to the method, describing what it does from an outside perspective.
    * Notice how the previously failing test `test_add_is_documented` now passes.
3. Repeat the above steps for the rest of the undocumented methods as indicated by the failing tests.

## Adding doctests

4. Expand the docstring for `add` with a doctest.
    * As we know that the implementation is correct, we can deliberately make the expectation in our doctest incorrect to verify that it runs and fails as expected.
    * Once we've seen the doctest fail, correct the expectation and see the doctest pass.
5. Compare the doctest to the existing test function `test_addition`.
    * As they test the exact same thing, we can keep the doctest and get rid of the test function.
6. Repeat the above steps for `subtract`, `multiply`, and `divide`.

## Documenting the class and the package

Docstrings can be used for more than just methods. 

7. Add a test that ensures that the `Recallculator` class is documented. Then add a docstring to the class briefly describing its purpose.
    * This can be done by checking `Recallculator.__doc__` and adding a docstring at the top of the class. 
8. Add a test that ensures that the `recallculator` package is documented. Then add a docstring to the package briefly describing its purpose.
    * This can be done by checking `recallculator.__doc__` and adding a docstring at the top of `__init__.py`.

## Reading the documentation in the REPL

9. Enter the Python REPL from this directory in the terminal. Use the `help` function in combination with whatever `import` statements you need to check the following:
    * The documentation for the package `recallculator`.
    * The documentation for the class `Recallculator`.
    * The documentation for the method `multiply`.
    * The documentation for the property `operations`.

## Bonus round (optional)

Doctests need not be done as a single line entered into the REPL with an expected response. We can use multiple lines though this tends to come with its own set of drawbacks. 

10. A doctest to `operations`.
    * Notice that you need to either assign the result of an executed line to a variable _or_ add the expected result below it.
        * If you decide to supress the result of the operations during the test setup, why is assigning the result to `_` like `>>> _ = calculator.add(1, 2)` a good idea?
    * Is this a suitable case for using a doctest rather than a normal test function?
