import pytest
import app.main as main


@pytest.mark.parametrize("word, expected", [
    # Casos base
    ("", True),                # string vazia é isograma
    ("a", True),               # letra única

    # True — sem repetição
    ("playgrounds", True),     # exemplo do enunciado
    ("abc", True),

    # False — com repetição
    ("look", False),           # exemplo do enunciado
    ("aa", False),             # repetição simples

    # Case-insensitive
    ("Adam", False),           # A e a são iguais
    ("Abc", True),             # maiúscula sem repetição
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected


def test_raises_on_wrong_type() -> None:
    with pytest.raises((TypeError, AttributeError)):
        main.is_isogram(123)
