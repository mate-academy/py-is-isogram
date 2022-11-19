from app.main import is_isogram


def test_return_isogram_with_lower_case() -> None:
    assert is_isogram("play") is True


def test_return_isogram_with_upper_case() -> None:
    assert is_isogram("Play") is True


def test_return_false_isogram_with_same_letters_lower_case() -> None:
    assert is_isogram("look") is False


def test_return_false_isogram_with_same_letters_upper_case() -> None:
    assert is_isogram("Adam") is False


def test_return_isogram_with_none_argument() -> None:
    assert is_isogram("") is True
