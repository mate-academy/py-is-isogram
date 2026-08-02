from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True, "An string is an isogram"


def test_all_capital() -> None:
    assert is_isogram("YES") is True, "YES is isogram"


def test_all_lower() -> None:
    assert is_isogram("hi") is True, "hi is isogram"


def test_mix_size_letters() -> None:
    assert is_isogram("pYTHon") is True, "pYTHon is isogram"


def test_not_isogram_capital_letters() -> None:
    assert is_isogram("GOOD") is False, "GOOD has repetition"


def test_not_isogram_lower_letters() -> None:
    assert is_isogram("assert") is False, "assert has repetition"


def test_not_isogram_mix_letters() -> None:
    assert is_isogram("helLon") is False, "helLon has repetition"


def test_isogram_symbols() -> None:
    assert is_isogram("!@#$") is True, "!@#$ is isogram"


def test_not_isogram_symbols() -> None:
    assert is_isogram("^-^") is False, "!^-^ has repetition"


def test_isogram_numbers() -> None:
    assert is_isogram("231") is True, "231 is isogram"


def test_not_isogram_numbers() -> None:
    assert is_isogram("094302") is False, "094302  has repetition"


def test_isogram_numbers_letters_symbols() -> None:
    assert is_isogram("aD1#") is True, "aD1# is isogram"


def test_not_isogram_numbers_letters_symbols() -> None:
    assert is_isogram("!tY9!") is False, "!tY9! has repetition"
