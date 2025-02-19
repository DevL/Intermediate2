import logging

logger = logging.getLogger(__name__)


def first(a, b):
    logger.warning("Calling first.")
    return second(a) + b


def second(x):
    logger.error("Calling second.")
    return x + 1
