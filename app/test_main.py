from app.main import is_isogram


def test_return_true_for_empty_string() -> None:
    assert is_isogram("") is True, \
        "Should return True for empty string"


def test_func_case_insensitive() -> None:
    assert is_isogram("Adam") is False, \
        "Function should be case-insensitive"


def test_long_isogram() -> None:
    assert is_isogram("playgrounds") is True, \
        "Playgrounds should be considered os isogram"


def test_not_isogram() -> None:
    assert is_isogram("look") is False, \
        "'look' should be considered as isogram"
