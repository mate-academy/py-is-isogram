from app.main import is_isogram


def test_true_for_playgrounds() -> None:
    assert is_isogram("playground")


def test_false_for_look() -> None:
    assert not is_isogram("look")


def test_is_case_sensitive() -> None:
    assert not is_isogram("Adam")


def test_true_for_empty_string() -> None:
    assert is_isogram("")
