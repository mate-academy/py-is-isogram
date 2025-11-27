import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "playground",
            True,
            id="is_isogram should return True for word with uniq letters",
        ),
        pytest.param(
            "p",
            True,
            id="is_isogram should return True for word with single letter",
        ),
        pytest.param(
            "look",
            False,
            id="is_isogram should return False for word with dupl letters",
        ),
        pytest.param(
            "",
            True,
            id="is_isogram should return True for empty string",
        ),
        pytest.param(
            "Adam",
            False,
            id="is_isogram should ignor different cases for symbols",
        ),
        pytest.param(
            "12345",
            True,
            id="is_isogram should accept string with numbers",
        ),
        pytest.param(
            "123455",
            False,
            id="is_isogram should accept string number and detect isogram",
        )
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_is_isogram_should_raise_attribute_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(1)
