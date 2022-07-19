import sys

import pytest

pytestmark = pytest.mark.skipif(
    sys.platform != 'win32',
    reason='Windows only tests',
)


def test_windows():
    pass
