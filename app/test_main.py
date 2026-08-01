from app.main import is_isogram


def test_zero_string() -> None:
    word = ""
    assert is_isogram(word)


def test_is_isogram() -> None:
    word = "pilot"
    assert is_isogram(word)


def test_not_isogram() -> None:
    word = "panama"
    assert not is_isogram(word)


def test_not_isogram_with_consecutive_letters() -> None:
    word = "apple"
    assert not is_isogram(word)


def test_not_isogram_with_capital_letters() -> None:
    word = "Mermaid"
    assert not is_isogram(word)
