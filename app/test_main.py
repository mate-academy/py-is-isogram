from app.main import is_isogram


def test_word_is_isogram() -> None:
    assert is_isogram('fork') == True
