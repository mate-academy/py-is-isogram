import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,check_isogram",
    [
        ("", True),
        ("a", True),
        ("A", True),
        ("playgrounds", True),
        ("PlAyGrOuNdS", True),
        ("look", False),
        ("LOOK", False),
        ("Adam", False),
        ("adam", False),
        ("ADAM", False)
    ]
)
def test_expected_result(word: str, check_isogram: bool) -> None:
    assert is_isogram(word) == check_isogram


@pytest.mark.parametrize(
    "word",
    [
        1, 1.5, False, ["a"], {"a": "a"}, {"a"}, ("a",)
    ]
)
def test_invalid_input_type(word: str) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)


@pytest.mark.parametrize(
    "word",
    [
        "134",
        "1Adam",
        "sdf_!%",
        "\nfr",
        "Hello,.",
        " ",
        "adam "
    ]
)
def test_invalid_input_value(word: str) -> None:
    with pytest.raises(ValueError):
        is_isogram(word)
