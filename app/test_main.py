from app.main import is_isogram


def test_checks_if_a_word_is_an_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("") is True
