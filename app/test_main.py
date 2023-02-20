import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True, id="Iso-word"),
    ]
)
def test_iso_word(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) is result


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("", True, id="Empty string")
    ]
)
def test_empty_string(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) is result


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("look", False, id="Consecutive letters")
    ]
)
def test_consecutive_letters(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) is result


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "Adam",
            False,
            id="Non-consecutive/case-insensitive letters"
        )
    ]
)
def test_nonconsecutive_and_case_insensitive_letters(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) is result
