# Packages

In a broad sense, a package is a collection of ideally consistent and coherent code and functionality. In Python, any file ending with `.py` is a module. A package typically consists of one or more Python modules. They can also contain nested packages.

The Python distribution comes with a number of packages as part of the language and its standard library comes with even more.
Additional packages can be installed from and uplodaded to a third-party source, such as [PyPI](https://pypi.org) (the Python Package Index). 

## The anatomy of a package

At a bare minimum, to create a Python package, you only need to create a directory and add an `__init__.py` module in it. The package name will be that of the directory and the contents will be that of the `__init__.py`. However, a more common way of organising a package is to have additional modules under the same directory and selectively import and export functionality via the `__init__.py` module.

An example of the file structure of a package follows.

```
mypackage/
    __init__.py
    module_a.py
    module_b.py
    subpackage/
        __init__.py
```

Given the above package structure, while one _could_ access a `thing` located in `module_b.py` by importing it like `from mypackage.module_b import thing`, it is often a good idea to make the desired `thing` available via the `__init__.py` module. 

Remember how Python doesn't have a true sense of private and protected as many other OOP languages do? It is still a good idea to signal what parts of our package are intended for public use and which are to be considered private implementation details that can be subject to change without breaking the "public" API of the package.

## Exercise 01

See _exercises/01_packages/instructions.md_.

## Additional Notes

The `__init__.py` is not strictly needed as of [PEP 420](
https://peps.python.org/pep-0420).
