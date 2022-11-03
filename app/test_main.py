import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,res",
    [
        ("", True),
        ("Adam", False),
        ("look", False),
        ("Playgrounds", True),
        ("WRTOdont", False)
    ]
)
def test_if_str_isogram_or_not(word: str,
                               res: bool) -> None:

    isogram = is_isogram(word)

    assert isogram == res
