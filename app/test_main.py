import app.main as main


def test_playgrounds_is_isogram() -> None:
    assert main.is_isogram("playgrounds") is True


def test_look_is_not_isogram() -> None:
    assert main.is_isogram("look") is False


def test_case_insensitive_check() -> None:
    assert main.is_isogram("Adam") is False


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True


def test_single_letter_is_isogram() -> None:
    assert main.is_isogram("a") is True


def test_non_consecutive_repeated_letters() -> None:
    assert main.is_isogram("aba") is False


def test_longer_word_with_repetition() -> None:
    assert main.is_isogram("programming") is False


def test_all_unique_mixed_case() -> None:
    assert main.is_isogram("Dermatoglyphics") is True


def test_detects_any_repeated_letter() -> None:
    assert main.is_isogram("abcdea") is False


def test_does_not_fail_on_all_unique_letters() -> None:
    assert main.is_isogram("lamp") is True
