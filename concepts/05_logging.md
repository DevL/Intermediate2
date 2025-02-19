# Logging

Python has robust and flexible support for logging built-in available through the [`logging`](https://docs.python.org/3.9/library/logging.html#module-logging) module. The same API can be used to log to the console, to a file, or to a third-party service over HTTP.

To understand and configure Python's logging support, there are four types of objects provided by the `logging` module.

To quote the documentation:

> **Loggers** expose the interface that application code directly uses.
>
> **Handlers** send the log records (created by loggers) to the appropriate destination.
>
> **Filters** provide a finer grained facility for determining which log records to output.
>
> **Formatters** specify the layout of log records in the final output.

We will primarily focus on the default use case of logging to the console and thus we will not delve deep into the latter three, but you should know that they exist and can be used to customize the way logs are output and stored. For example, to log to a file you would use a different `handler` object than the default one that logs to the terminal.

## Logging at different levels

Not all log messages are of equal importance. For that reason, a log can be written using a certain _level_ or _severity_. From the least important to the most, the levels are:

* **DEBUG**
* **INFO**
* **WARNING**
* **ERROR**
* **CRITICAL**

There are coresponding methods on `logger` objects to log messages at the desired level, for example `logging.info("some non-critical info")` will log at the **INFO** level. 

Depending on what level of logging your Python program is configured to use, some log messages will be supressed. A program with the log level set at the **WARNING** level will ignore any attempts to log at the **DEBUG** or **INFO** levels.   

## Resources

The Python documentation comes with a set of tutorials that explain logging in various detail.

* [Basic tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
* [Advanced tutorial](https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial)
* [Logging cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)

## Exercise 05

See _exercises/05_logging/instructions.md_.
