from app.main import is_isogram


def test_empty_string():
    assert is_isogram('')


def test_mix_upper_with_lower():
    assert not is_isogram('Adam')


def test_string_without_repeating():
    assert is_isogram('playgrounds')


def test_all_letters_repeat():
    assert not is_isogram("bbbBBBBbb")

