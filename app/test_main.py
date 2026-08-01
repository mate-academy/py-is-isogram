from app.main import is_isogram


def test_no_repeating_letters() -> None:
    assert is_isogram("nightmare")


def test_repeating_letters() -> None:
    assert not is_isogram("boss")


def test_no_letters() -> None:
    assert is_isogram("")


def test_consecutive_word() -> None:
    assert not is_isogram("SOS")


def test_lower_and_upper_case() -> None:
    assert not is_isogram("preSs")
