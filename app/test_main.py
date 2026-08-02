from app.main import is_isogram


def test_if_string_is_empty() -> None:
    assert is_isogram("") is True


def test_not_a_single_symbol() -> None:
    assert is_isogram("sweet") is False


def test_upper_case() -> None:
    assert is_isogram("Trait") is False


def test_different_upper_case() -> None:
    assert is_isogram("pLaYgRoUnD") is True


def test_same_upper_letter() -> None:
    assert is_isogram("lOok") is False


def test_correct_string() -> None:
    assert is_isogram("playgrounds") is True
