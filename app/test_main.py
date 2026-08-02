import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,true_or_false",
    [
        pytest.param("", True),
        pytest.param("look", False),
        pytest.param("ADAM", False),
        pytest.param("MiX", True),
        pytest.param("Aa", False),
        pytest.param("qwertyuiopasdfghjklzxcvbnm", True)
    ]
)
def test_only_letters(word: str, true_or_false: bool) -> None:
    assert is_isogram(word) is true_or_false
