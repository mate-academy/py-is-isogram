from app.main import is_isogram


def test_can_detect_isogram() -> None:
    assert (
        is_isogram("playgrounds") is True
    ), "'playgrounds' is an isogram."


def test_can_detect_not_isogram() -> None:
    assert (
        is_isogram("look") is False
    ), "'look' is not an isogram."


def test_can_detect_empty_string() -> None:
    assert (
        is_isogram("") is True
    ), "'' is an isogram."


def test_can_be_case_insensitive() -> None:
    assert (
        is_isogram("Adam") is False
    ), "'Adam' is not an isogram."
