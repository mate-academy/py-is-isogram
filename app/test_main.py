from app.main import is_isogram

def test_check_the_empty_string():
    result = is_isogram("")
    assert result is True


def test_check_isogramic_word():
    result = is_isogram("playgrounds")
    assert result is True


def test_check_not_isogramic_word():
    result = is_isogram("look")
    assert result is False


def test_check_not_isogramic_word_with_two_registers():
    result = is_isogram("Adam")
    assert result is False
