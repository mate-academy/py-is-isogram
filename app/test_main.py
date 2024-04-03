from app.main import is_isogram


def test_when_a_word_is_an_isgram() -> None:
    result = (is_isogram("playgrounds"))
    assert result is True

def test_when_a_word_is_not_an_isgram() -> None:
    result = (is_isogram("look"))
    assert result is False


def test_if_the_string_is_empty() -> None:
    result = (is_isogram(""))
    assert result is True


def test_to_check_case_sensitivity_of_letters() -> None:
    result = (is_isogram("LoOk"))
    assert result is False


def test_when_a_word_is_not_an_isgram_2() -> None:
    result = (is_isogram("Adam"))
    assert result is False