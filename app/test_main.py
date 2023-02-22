from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_similar_letters_case() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("aac") is False
