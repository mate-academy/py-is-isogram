import app.main as main


def test_empty_string() -> None:
    assert main.is_isogram("") is True


def test_single_letter() -> None:
    assert main.is_isogram("a") is True


def test_simple_isogram() -> None:
    assert main.is_isogram("playgrounds") is True


def test_repeating_letters() -> None:
    assert main.is_isogram("look") is False


def test_case_insensitive_false() -> None:
    assert main.is_isogram("Adam") is False


def test_case_insensitive_true() -> None:
    assert main.is_isogram("Dermatoglyphics") is True


def test_all_same_letters() -> None:
    assert main.is_isogram("aaaa") is False


def test_non_consecutive_repeats() -> None:
    assert main.is_isogram("alphabet") is False


def test_mixed_case_isogram() -> None:
    assert main.is_isogram("Machine") is True


def test_long_isogram() -> None:
    assert main.is_isogram("subdermatoglyphic") is True
