from app.main import is_isogram


def test_empty_string_must_be_true():
    assert is_isogram("")


def test_word_with_doubled_letter():
    assert not is_isogram("look")


def test_capitalized_word_with_repeating():
    assert not is_isogram("Adam")


def test_right_isogram_word():
    assert is_isogram("playgrounds")
