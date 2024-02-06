
from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True, "Error on 'playgrounds'"
    assert is_isogram("look") is False, "Error on 'look'"
    assert is_isogram("Adam") is False, "Error on 'Adam'"
    assert is_isogram("") is True, "Error on ''"
