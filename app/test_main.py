import pytest

from app.main import is_isogram


def test_returns_bool() -> None:
    assert (
        isinstance(is_isogram("snowman"), bool)
    )


@pytest.mark.parametrize(
    "word",
    [
        pytest.param(1, id="Raises TypeError when int"),
        pytest.param(705.423, id="Raises TypeError when float"),
        pytest.param(True, id="Raises TypeError when bool"),
        pytest.param(["a", "b"], id="Raises TypeError when list"),
    ]
)
def test_raises_error_when_wrong_datatype(word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("book", False),
        ("KAWOBING", True),
        ("WATERMELON", False)
    ]
)
def test_letters_in_same_register(word: str, expected: bool) -> None:
    assert (
        is_isogram(word) == expected
    )


@pytest.mark.parametrize(
    "word,expected",
    [
        ("coOl", False),
        ("anNA", False),
        ("wxxxxxxxxxxxW", False)
    ]
)
def test_letters_in_different_registers(word: str, expected: bool) -> None:
    assert (
        is_isogram(word) == expected
    )


def test_empty_str_returns_true() -> None:
    assert (
        is_isogram("") is True
    )
