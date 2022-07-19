from os import environ

import pytest

in_ci = 'CI' in environ
ci_only = pytest.mark.skipif(not in_ci, reason='not in CI')


def test_always():
    pass


@ci_only
def test_in_ci():
    pass


@pytest.mark.web
def test_web():
    pass
