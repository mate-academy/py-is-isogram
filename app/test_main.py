from app.main import is_isogram


def test_unique_word() -> None:
    assert is_isogram("playgrounds") == True


def test_repeated_letters() -> None:
    assert is_isogram("look") == False


def test_non_unique_word() -> None:
    assert is_isogram("Adam") == False


def test_just_a_string() -> None:
    assert is_isogram("") == True
