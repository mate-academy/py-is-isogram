from app.main import is_isogram


def test_is_isogram_with_empty_string() -> None:
    result = is_isogram('')
    assert result is True, f"Expected True but got {result}"


def test_is_isogram_with_isogram_word() -> None:
    result = is_isogram('playgrounds')
    assert result is True, f"Expected True but got {result}"


def test_is_isogram_with_non_isogram_word() -> None:
    result = is_isogram('look')
    assert result is False, f"Expected False but got {result}"


def test_is_isogram_with_mixed_case_word() -> None:
    result = is_isogram('Adam')
    assert result is False, f"Expected False but got {result}"


def test_is_isogram_with_case_insensitive_word() -> None:
    result = is_isogram('MoOse')
    assert result is False, f"Expected False but got {result}"
