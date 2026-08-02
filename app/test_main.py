from app.main import is_isogram


def test_isogram_is_true() -> None:
    assert (is_isogram("playgrounds") is True
            ), "this word has no repeat"


def test_upper_lower_case() -> None:
    assert (is_isogram("Adam") is False
            ), "upper and lower case should be one letter"


def test_isogram_false_value() -> None:
    assert (is_isogram("look") is False
            ), "this word has repeat letter"


def test_empty_str() -> None:
    assert (is_isogram("") is True
            ), "empty str is isogram"
