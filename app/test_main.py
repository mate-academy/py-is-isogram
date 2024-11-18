from app.main import is_isogram


def test_is_isogram_have_to_be_true_empty_string() -> None:
    assert (
        is_isogram("") is True
    ), "Is isogram have to be true empty string"


def test_is_isogram_have_to_be_true_playgrounds() -> None:
    assert (
        is_isogram("playgrounds") is True
    ), "Is isogram have to be true playgrounds"


def test_is_isogram_have_to_be_false_and_check_case_adam_string() -> None:
    assert (
        is_isogram("Adam") is False
    ), "Is isogram have to be False and check case Adam string"


def test_is_isogram_have_to_be_false_look_string() -> None:
    assert (
        is_isogram("look") is False
    ), "Is isogram have to be False look string"
