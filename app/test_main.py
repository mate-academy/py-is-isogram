import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("playgrounds", True, id="'playgrounds' - True"),
        pytest.param("look", False, id="'look' - False"),
        pytest.param("Adam", False, id="'Adam' - False"),
        pytest.param("", True, id="'' - True"),
        pytest.param("123", True, id="'123' - True"),
        pytest.param("1233", False, id="'1233' - False"),
        pytest.param("  ", False, id="'  ' - False"),
        pytest.param(" ", True, id="' ' - True"),
        pytest.param(".,-", True, id="'.,-' - True"),
        pytest.param(",,,", False, id="',,,' - False"),
    ]
)
def test_should_return_correct_value(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
