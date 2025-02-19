from argparse import ArgumentParser
import logging
import mypackage

ALLOWED_LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
DEFAULT_LOG_LEVEL = logging.WARNING


def main():
    args = _parse_command_line_args()
    _configure_logging(args.log_level)

    mypackage.hello()
    logging.info("Just called hello, now on to calling first.")
    mypackage.first(1, 2)

    if args.book_tip:
        _give_book_tip()
    else:
        logging.critical("It's a good book tip, don't miss it!")


def _parse_command_line_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-l",
        "--log-level",
        help=f"set the log level ({', '.join(ALLOWED_LOG_LEVELS)})",
    )
    parser.add_argument(
        "-b",
        "--book-tip",
        help="give a book tip",
        action="store_true",
    )
    return parser.parse_args()


def _configure_logging(level_input):
    log_level = _get_log_level(level_input)
    log_file = "lumberjack.log"
    logging.basicConfig(
        filename=log_file,
        filemode="w",
        level=log_level,
    )
    logging.debug("Logging configured.")


def _get_log_level(level_input):
    if not level_input:
        return DEFAULT_LOG_LEVEL

    level_candidate = level_input.upper()

    if level_candidate in ALLOWED_LOG_LEVELS:
        return getattr(logging, level_candidate)
    else:
        return DEFAULT_LOG_LEVEL


def _give_book_tip():
    print(
        "For a great book on object-oriented programming, look no further than",
        "\t99 Bootles of OOP",
        "by Sandi Metz, Katrina Owen, and TJ Stankus",
        sep="\n",
    )


if __name__ == "__main__":
    main()
