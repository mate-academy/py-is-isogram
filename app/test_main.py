import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),   # exemplo positivo
        ("look", False),         # repetição não consecutiva
        ("", True),              # string vazia é isograma
        ("a", True),             # limite: 1 caractere
    ],
)
def test_is_isogram_examples_and_edges(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_is_isogram_case_insensitive_true() -> None:
    # Mesmo com letras maiúsculas diferentes, nenhuma se repete
    assert is_isogram("Dermatoglyphics") is True


def test_is_isogram_case_insensitive_false() -> None:
    # Mesma letra em casos diferentes deve contar como repetição
    assert is_isogram("Adam") is False
    assert is_isogram("moOse") is False
