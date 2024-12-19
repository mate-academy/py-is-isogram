from app.main import is_isogram


def test_is_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_false() -> None:
    assert is_isogram("moon") is False


def test_is_isogram_capital_false() -> None:
    assert is_isogram("mOon") is False


def test_is_isogram_capital_true() -> None:
    assert is_isogram("Sun") is True


def test_is_isogram_empty() -> None:
    assert is_isogram("") is True


def test_is_isogram_numeric_true() -> None:
    assert is_isogram("1234") is True


def test_is_isogram_numeric_false() -> None:
    assert is_isogram("12343") is False
