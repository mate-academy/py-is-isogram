from app.main import is_isogram


def test_is_isogram_gap() -> None:
    assert is_isogram("")


def test_is_isogram_lower_case() -> None:
    assert not is_isogram("Adam")


def test_is_isogram_upper_case() -> None:
    assert not is_isogram("LOOK")


def test_is_isogram_neighb_letter() -> None:
    assert not is_isogram("letter")


def test_is_isogram_begin_of_word() -> None:
    assert not is_isogram("aab")


def test_is_isogram_end_of_word() -> None:
    assert not is_isogram("abb")


def test_is_isogram_same_first_and_last_letters() -> None:
    assert not is_isogram("abra")


def test_is_isogram_one_letter() -> None:
    assert is_isogram("a")
