import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Alphabet", False),
        ("isogram", True),
        ("subdermatoglyphic", True),
        ("mMoO", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    # ANN201: Anotación de retorno para cumplir con flake8
    assert is_isogram(word) is expected


def test_is_isogram_should_be_case_insensitive() -> None:
    # Verificamos explícitamente que 'A' y 'a' se consideren iguales
    assert is_isogram("Adam") is False


def test_empty_string_is_an_isogram() -> None:
    # Caso borde: el string vacío no tiene letras repetidas
    assert is_isogram("") is True
