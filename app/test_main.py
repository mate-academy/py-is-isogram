from app.main import is_isogram


def test_is_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_false() -> None:
    assert is_isogram("look") is False


def test_is_isogram_false_caseintensive() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_empty() -> None:
    assert is_isogram("") is True
