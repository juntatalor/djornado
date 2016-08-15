import pytest

from project.application.utils import make_password, check_password


def test_utils():
    p = make_password('Secret password')
    assert p == b'e06e565e5974ae1d3e30543068f6020b556cee901d79e8e1d04b6e73dcc048d3'

    with pytest.raises(AssertionError):
        assert check_password('Another secret password', p)
