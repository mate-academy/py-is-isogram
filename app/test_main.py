from app.main import is_isogram
from pytest import mark, raises, param


@mark.parametrize(
    "word,expected_result",
    [
        param("", True,
              id="should return true string is empty"),
        param("playgrounds", True,
              id="should return true if string no has the same letters"),
        param("food", False,
              id="should return false if string has the same letters"),
        param("Adam", False,
              id="should return false if string has the same letters"
                 "in different cases")
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result


def test_raise_error_if_type_of_value_is_incorrect() -> None:
    with raises(TypeError):
        is_isogram(12)
