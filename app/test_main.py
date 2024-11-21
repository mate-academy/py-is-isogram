from app.main import is_isogram


def test_word_is_an_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_word_missing() -> None:
    assert is_isogram("") is True


def test_word_is_repeated() -> None:
    assert is_isogram("Adam") is False


def test_with_spaces() -> None:
    assert is_isogram("playg rounds") is True


def test_word_with_hyphens() -> None:
    assert is_isogram("playg-rounds") is True
