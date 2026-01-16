from app.main import is_isogram
import pytest


@pytest.mark.parametrize("initial_string,expected_output", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    pytest.param("h",
                 True,
                 id="single letter"),
    pytest.param("abcdefghijklmnopqrstuvwxyz",
                 True,
                 id="full alpha isogram"),
    pytest.param("abcdefghijklmnopqrstuvwxyzW",
                 False,
                 id="long isogram False"),
])
def test_is_isogram(initial_string: str, expected_output: bool) -> None:
    assert is_isogram(initial_string) == expected_output
