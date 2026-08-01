from app.main import is_isogram


def test_should_check_with_diplicates() -> None:
    word = "look"
    expected_result = False
    result = is_isogram(word)
    assert result == expected_result


def test_should_check_zero_string() -> None:
    word = ""
    expected_result = True
    result = is_isogram(word)
    assert result == expected_result


def test_should_check_long_word() -> None:
    word = "playgrounds"
    expected_result = True
    result = is_isogram(word)
    assert result == expected_result


def test_should_check_different_registers() -> None:
    word = "Adam"
    expected_result = False
    result = is_isogram(word)
    assert result == expected_result
