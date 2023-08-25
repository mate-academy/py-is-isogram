import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("Word", True),
        ("ComPuter", True)
    ]
)
def test_should_return_true(word: str, result: bool) -> None:
    result = is_isogram(word)
    assert result is True


@pytest.mark.parametrize(
    "word, result",
    [
        ("Success", False),
        ("OcLock", False)
    ]
)
def test_should_return_false(word: str, result: bool) -> None:
    result = is_isogram(word)
    assert result is False
