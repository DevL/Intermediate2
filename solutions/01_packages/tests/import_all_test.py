import pytest
from mypackage import *


def test_import_all():
    assert first(2, 3) == 6
    assert hello() == "Hello, I'm in a package."


def test_all_excludes_even_public_things_if_they_have_not_been_listed():
    """
    The trailing comment on the assertion line is to supress a Pylance warning about
    a variable being undeclared. We expect it not to exist in this particular case.
    """
    with pytest.raises(NameError, match="name 'this_is_public' is not defined"):
        assert this_is_public == 1  # type: ignore
