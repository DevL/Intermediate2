# Exercise 02 - TDD

We will be creating a tiny calculator package using TDD.

## Intended Usage

We intend for the package to contain a `Recallculator` class. 
Each instance of `Recallculator` will keep track of all the operations it performs and we will be able to get a list of them.

## Creating and importing the package

1. In this directory, create a directory called `tests`.
2. In the `tests` directory, create a test module called `recallculator_test.py`. 
3. At the top of the test module, import the `Recallculator` class from the `recallculator` package.
    * Note that neither exists yet. This is intentional. Our test run will tell us to create them.
4. Run the tests, e.g. run `pytest` in the terminal from the _exercises/02_tdd_ directory.
    * You should get a `ModuleNotFoundError: No module named 'recallculator'` error.
5. Fix the error by creating a package called `recallculator`. The `__init__.py` module can be completely empty.
    * Running the tests again should now yield the error `ImportError: cannot import name 'Recallculator' from 'recallculator'`.
6. Fix the error by creating an empty class `Recallculator` in the `__init__.py` file.
    * You can use `pass` as the body of the class.
    * Running `pytest` will no longer result in any import error.
        * While pytest states that it doesn't find any tests to run, there was an implicit import test that we used to go from red to green.

## Adding our first test

What do we know about this recalling calculator of ours? Regardless of the operations it can perform and recall, we know that a new instance should have an empty list of performed operations.  

7. Create a test function called `test_a_new_instance_has_not_performed_any_operations`. In it, create an instance of `Recallculator` and assert that the instance's list of operations is empty. 
    * Assuming that the instance is called `calculator` this could look like `assert calculator.operations == []`.
8. Running the test, we should see the error `AttributeError: 'Recallculator' object has no attribute 'operations'`.
    * Fix the error by making sure that a `Recallculator` instance is initialized with an `operations` attribute.
    * Bonus points if you first set it to `None`, then run the tests again, and _only then_ sets it to an empty list.
        * Note how pytest outputs our object. We can make that nicer and more readable by implementing `__repr__`.
        
Hey! Our first properly passing test that shows up as green! There's not much to refactor at this point so we move on.

## Adding addition

Let's implement addition. This will also make us start storing performed operations.

9. Create a test function called `test_addition`. In it, create an instance of `Recallculator`, send it the `add` message with two numbers as arguments, and assert that the result is the sum.
    * Running the test will show us that we don't have an `add` method. Add one that doesn't have any parameters other than `self`.
        * You can use `pass` as its body.
    * Running the tests a second time will show us that we don't accept the correct number of arguments. Add the missing parameters to the method definition and re-run the test.
    * We now need to sum the passed arguments and return the result. This should give us a green test.  

But we also want to see that the operation was stored. This _could_ be done as a second assertion added to the same test, but often it's better to strive for a single assertion per test – especially when _driving_ the design of a piece of code through tests.

10. Create a test called `test_registering_addition`. In it, create an instance, send it the `add` message as above, but now assert that the instance's `operations` attribute is a list containing an element looking like this (assuming `1` and `2` was passed as arguments to `add`): `"1 + 2"`
    * As before, run the tests and make the smallest possible changes to the code to make it pass.
        * If you're tempted to hardcode the `"1 + 2"` string as the contents of `operations`, add another test that adds a different set of numbers and expects a different operation registered.

What happens if we perform two operations? In which order are they registered? Let's decide that they should be listed in reverse chronological execution order, i.e. first performed, last listed.

11. Add a test called `test_registering_multiple_operations`.
    * Perform two addition operations using the same instance and then assert that its operations list contains the expected strings in the intended order.
12. We might not have much code to refactor yet, but we do have a number of test cases that all starts by creating an instance of `Recallculator`. We could use a pytest fixture to remove that repetitiveness.

## Adding subtraction, multiplication, and division

13. To add subtraction we follow the same principal as for adding support for addition from step 9 and onwards.
    * Notice how we start seeing some recurring patterns. Be patient in extracting helper methods though. A good rule of thumb is to allow until the third occurance of what seems to be a pattern before extracting. We're not there yet.
14. Now that we also have added multiplication, we might notice that we register operations in a similar manner in our `add`, `subtract`, and `multiply` methods.
    * Make sure that all tests passes. Refactoring is **only** done with green tests.
    * Add a `_register_operation` method to `Recallculator`. Use it from `add`, `subtract`, and `multiply` instead of changing `self.operations` directly from those methods.
    * Notice how all tests still pass as we're only chaning _structure_, not _behaviour_ when refactoring. If you see a failing test during this process, something is amiss.
15. Add division using the `_register_operation` method. Remember - tests first!

## Refining our tests

Now that we support the four ways of counting, we can refine our tests a little. In particular the one called `test_registering_multiple_operations`. 

16. Change the operations performed and listed. As we are changing a test we rather than the behaviour of the code under test we can start by changing what our _actual_ is, i.e. what operations we perform, and _then_ run the test once to see that it's red. This tells us that our _expectations_ are incorrect. Updating our expected list of performed operations will fix this.
    * We could even consider getting rid of the individual tests that check if a certain operation is being registered if we include them all in this test.

## Bonus round (optional)

Storing the operations in reverse order by concating two lists is a rather expensive operation compared to appending an element to an existing list. We might also assume that we more often perform operations than we retrieve the list of operations performed. 

17. Use a private attribute `_operations` to store the performed operations in execution order (first in, first listed) and a property `operations` that returns the contents of `_operations` in reverse. As we have isolated the registration of operations to the `_register_operations` method, we can change it from concating two lists to appending to the `_operations` list instead.

Also, let's practice refactoring and package organisation a bit more.

18. We have all logic in the `__init__.py` module. Move the `Recallculator` class into a submodule instead and make sure that no tests break during the process by importing and exporting it properly.

19. We previously mentioned that we could add a `__repr__` implementation. When possible, `__repr__` should return a string representation usable to create a copy of the instance in the Python REPL. But as we can't initalize an instance with a set of performed operations, we will instead show the number of operations performed by the instance.
    * Aim for this format: `<Recallculator, operations: 5>` 

## Solution notes

Three sets of tests have been provided.

* The first covers steps 1-11: _solutions/02_tdd_part_1_  
* The second covers steps 12-16: _solutions/02_tdd_part_2_  
* The third covers steps 17-19: _solutions/02_tdd_part_3_  

Run them by entering into respective directory in the terminal and run `pytest`.
