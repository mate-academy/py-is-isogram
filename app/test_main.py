from app.main import is_isogram


def test_is_empty_string() -> None:
    assert is_isogram("")


def test_repeating_lower_case_letters() -> None:
    assert not is_isogram("look")


def test_repeating_upper_case_letters() -> None:
    assert not is_isogram("LOOK")


def test_repeating_mixed_case_letters() -> None:
    assert not is_isogram("Adam")


def test_true_isogram() -> None:
    assert is_isogram("playground")
