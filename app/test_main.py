import app.main as main_module


def test_isogram_simple_true() -> None:
    assert main_module.is_isogram("playgrounds") is True


def test_isogram_simple_false() -> None:
    assert main_module.is_isogram("look") is False


def test_isogram_case_insensitive_false() -> None:
    assert main_module.is_isogram("Adam") is False


def test_isogram_empty_string_true() -> None:
    assert main_module.is_isogram("") is True


def test_isogram_single_letter_true() -> None:
    assert main_module.is_isogram("a") is True


def test_isogram_all_unique_mixed_case_true() -> None:
    assert main_module.is_isogram("Dermatoglyphics") is True
