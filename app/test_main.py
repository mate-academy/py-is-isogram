import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("Alphabet", False),
    ],
    ids=[
        "valid_isogram",
        "repeated_consecutive",
        "case_insensitive_repeat",
        "empty_string",
        "common_isogram",
        "case_insensitive_alphabet"
    ]
)
def test_is_isogram_examples(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


@pytest.mark.parametrize(
    "invalid_input",
    [123, [1, 2, 3], None],
    ids=["integer_input", "list_input", "none_input"]
)
def test_is_isogram_raises_type_error(invalid_input: any) -> None:
    with pytest.raises(TypeError):
        is_isogram(invalid_input)


def test_is_isogram_case_insensitivity() -> None:
    # Garante que letras maiúsculas e minúsculas são tratadas como iguais
    assert is_isogram("AbCda") is False
