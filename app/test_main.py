from app.main import is_isogram


# --- Basic examples from the spec ---
def test_playgrounds_is_isogram() -> None:
    assert is_isogram('playgrounds') is True

def test_look_is_not_isogram() -> None:
    assert is_isogram('look') is False

def test_adam_is_not_isogram_case_insensitive() -> None:
    assert is_isogram('Adam') is False

def test_empty_string_is_isogram() -> None:
    assert is_isogram('') is True


# --- Case insensitivity ---
def test_all_uppercase_isogram() -> None:
    assert is_isogram('ABCDE') is True

def test_mixed_case_repeated_letter() -> None:
    assert is_isogram('Aa') is False

def test_mixed_case_isogram() -> None:
    assert is_isogram('SubDermal') is True


# --- Single character ---
def test_single_char_is_isogram() -> None:
    assert is_isogram('a') is True

def test_single_uppercase_char_is_isogram() -> None:
    assert is_isogram('Z') is True


# --- Repeated letters ---
def test_consecutive_repeated_letters() -> None:
    assert is_isogram('aa') is False

def test_non_consecutive_repeated_letters() -> None:
    assert is_isogram('aba') is False

def test_repeated_letter_at_end() -> None:
    assert is_isogram('abca') is False


# --- Longer valid isograms ---
def test_isogram_longer_word() -> None:
    assert is_isogram('background') is True

def test_isogram_thumbscrew() -> None:
    assert is_isogram('thumbscrew') is True

def test_non_isogram_longer_word() -> None:
    assert is_isogram('eleven') is False
