import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
        pytest.param("", True),
    ]
)
def test_is_isogram(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(24, TypeError),
        pytest.param(["playgrounds"], TypeError),
        pytest.param([True], TypeError),
    ]
)
def test_is_isogram_with_type_error(
        word: str,
        expected: type[TypeError]
) -> None:
    with pytest.raises(expected):
        is_isogram(word)


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(" playgrounds", ValueError),
        pytest.param("lo k ", ValueError),
        pytest.param("A D a m", ValueError),
    ]
)
def test_is_isogram_with_spaces_error(
        word: str,
        expected: type[ValueError]
) -> None:
    with pytest.raises(expected):
        is_isogram(word)
