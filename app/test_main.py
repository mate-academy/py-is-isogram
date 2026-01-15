import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word_, bool_",
                         [
                             # when word is too big and only one copy
                             ("qwertyuiopasdfghjklzxcvbnm", True),
                             # when word with numbers
                             ("Lol182", False),
                             ("qol182", False),
                             # if word is empty
                             ("", True),
                             # simple tests
                             ("jecdhdaj", False),
                             ("jecqiqiqiq", False),
                             ("adhaisdi", False),
                             ("qwuhnfi", True)])
def test_universal(word_: str, bool_: bool) -> None:
    result = is_isogram(word_)
    assert result == bool_


def test_atribute() -> None:
    word = []
    with pytest.raises(AttributeError):
        is_isogram(word)
