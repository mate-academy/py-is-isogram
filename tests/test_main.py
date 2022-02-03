from app.main import is_isogram


def test_empty_string():
    goal = is_isogram("")

    assert goal is True


def test_with_uppercase_letters():
    goal = is_isogram("PlaygRound")

    assert goal is True


def test_with_symbls_spaces_and_digits():
    goal = is_isogram("abcdefg7. $")

    assert goal is True
