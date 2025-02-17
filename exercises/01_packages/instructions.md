# Exercise 01 - Packages

We will be creating a tiny package that only exposes some of its functionality, import it into a Python REPL and examine it.

1. In this directory, create another directory.
    * The directory name will be the name of the package.
    * The name should follow the [PEP 8 conventions](https://peps.python.org/pep-0008/#package-and-module-names).
    * If you don't know what to call it, name it `mypackage`.
2. Create an `__init__.py` module in the package directory.
3. Add a function to this module. It can do anything you like.
4. Create another Python module in the package directory.
    * The name should follow the [PEP 8 conventions](https://peps.python.org/pep-0008/#package-and-module-names).
    * If you don't know what to call it, name it `my_module.py`. 
5. Add two functions to your submodule. Call them what you like, but here they'll be referred to as `first` and `second`.
    * Have the first function call the other function, returning its result.
    * Have the second function return some value, either calculated or fixed.
6. In the `__init__.py` module, import the first function, but not the second function.
    * See [`import` from submodules](https://docs.python.org/3.9/reference/import.html#submodules).
7. Signal that the imported function as well as the one you created in step 3 are the public API of this package.
    * You do this by declaring `__all__`. It should be a list of strings listing the public functions and variables. For in-depth information, see [`import`](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement).
8. To test things in a Python REPL, run `python` from the `01_packages` directory in the terminal.
    * If you run `import mypackage` in the REPL you can access the first function as `mypackage.first`. Can you access the second one in the same manner? If not, why not?
    * If you run `from mypackage import *`, you should be able to call your exported functions without `mypackage.` in front of them.

## Bonus round (optional)

9. How can you access the second function even though it hasn't been exported?
10. What happens if you add another function to `__init__.py`, restart the REPL, and run `from mypackage import *`?
    * What role does `__all__` play in this?
    * What happens if you remove `__all__`?
    * What happens if you also make the function "private" by prefixing it with an underscore?


## Solution notes

Tests have been provided. Run them by entering into the _solutions/01_packages_ directory in the terminal and run `pytest`.
