# Exercise 05 - Logging

You will be adding logging at various levels to an existing Python program and examine the output by running the program at various log levels.

You can run the program from this directory with `python lumberjack.py`.
By default there will be no output listed, but you can access the help by running `python lumberjack.py -h` or `python lumberjack.py --help`.

## Examining the program

Before you proceed, study `lumberjack.py` and answer the following questions.

1. You should avoid adding any log messages before [`logging.basicConfig`](https://docs.python.org/3.9/library/logging.html#logging.basicConfig) has been called. Why?
2. If no log level is set on the command line, which log level will the program use?
    * Did you just read the constant name?
3. Why is the supplied log level converted into uppercase in the `_get_log_level` function?
    * Hint: have a look at how [`getattr`] works.
    * Hint: import `logging` in a REPL and see what `dir(logging)` returns.
4. What does the conditional early return in `_get_log_level` guard against?
    * Hint: comment it out and run the program without any options on the command line.
5. What happens if you run the program with the log level set to debug from the command line?
    * If you wonder how to do this, run `python lumberjack.py -h` to read the help text. 

## Add log messages at various levels

Now that you have a grasp of the program, it is time to add some log messages to it. 

6. Add a log message at the **INFO** level after calling `hello`, but before calling `first`.
    * Run the program. What do you need to make the log message show up in the terminal?
7. Add log messages to both functions in `mypackage.mymodule`.
    * Use two different log levels. 
8. Add a log message indicating that no book tip was requested.

## Module-specific logging

We have been using the root logger. But it is possible to create and use separate loggers for each module. To do so, one adds the line `logger = logging.getLogger(__name__)` after importing `logging`. After that, use `logger.info(...)` instead of `logging.info(...)`. 

9. Update `mypackage.mymodule` to create a logger as per above and use it from the functions `first` and `second`.
    * Run the program and study the log messages. What has changed?
10. Why do we use `__name__` as the argument to `logging.getLogger`? What happens if we change it to an arbitrary string?
    * Run the program and study the log messages. What has changed?

## Logging to a file

11. Update the logging configuration so that the logs are written to a file called `lumberjack.log` instead of being output to the terminal.
    * Hint: have a look at the `filename` option for [`logging.basicConfig`](https://docs.python.org/3.9/library/logging.html#logging.basicConfig).
    * Run the program a few times at various log levels and study the log file to see what happens.
12. Update the logging configuration to overwrite the logfile rather than append to it every time the program runs.
    * Hint: have a look at the `filemode` option for [`logging.basicConfig`](https://docs.python.org/3.9/library/logging.html#logging.basicConfig),

## Bonus round (optional)

Our program uses the [`argparse`](https://docs.python.org/3/library/argparse.html) module to handle the command line options. Use this to make our logging even more configurable!

13. Add an optional command line option `-f` and `--log-file` that specifies the filename to log to. If it is given, log to that file. If not, output the logs to the terminal.
    * Hint: what happens if the `filename` option for [`logging.basicConfig`](https://docs.python.org/3.9/library/logging.html#logging.basicConfig) is set to `None`?
14. Add an optional command line option `-m` and `--log-file-mode` that specifies the way logs should be written to a logfile. Allow the options `append` and `overwrite`.

## Solution notes

An example solution for exercises 6-9 and 11-12 can be found in the _solutions/05_logging_ directory.
