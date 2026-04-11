import pytest
from app.main import is_isogram


@pytest.mark.parametrize("s", ["", "playgrounds", "a"])
def test_isogram_true(s):
    assert is_isogram(s)
@pytest.mark.parametrize("s", ["look", "Adam", "aA", "local"])
def test_isogram_false(s):
    assert not is_isogram(s)
