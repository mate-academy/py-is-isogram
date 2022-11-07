from app.main import is_isogram


def test_should_return_true_if_func_accepts_an_empty_string() -> None:
    assert (
        is_isogram("")
    )


def test_should_be_case_insensitive() -> None:
    assert (
        is_isogram("Adam") is False
    )


def test_should_work_for_consecutive_letters() -> None:
    assert (
        is_isogram("look") is False
    )
