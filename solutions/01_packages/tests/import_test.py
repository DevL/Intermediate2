import mypackage


def test_import():
    assert mypackage.first(1, 2) == 4
    assert mypackage.hello() == "Hello, I'm in a package."
    assert mypackage.this_is_public == 1
    assert mypackage._this_is_private == 2
