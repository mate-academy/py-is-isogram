from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") == True
    assert is_isogram("look") == False
    assert is_isogram("Adam") == False
    assert is_isogram("") == True
    assert is_isogram("isogram") == True
    assert is_isogram("subdermatoglyphic") == True
    assert is_isogram("Alphabet") == False
