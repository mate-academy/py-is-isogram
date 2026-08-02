from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, actual",
    [
        pytest.param("a", True, id="One letter"),
        pytest.param("", True, id="Empty string"),
        pytest.param("Adam", False, id="Letters big and small -> False"),
        pytest.param("PlayGrounds", True, id="Letters big and small -> True"),
        pytest.param("look", False, id="Adjacent identical letters -> False"),
    ]
)
def test_is_isogram(word: str, actual: bool) -> None:
    assert is_isogram(word) is actual

# from app.main import is_isogram
#
#
# def test_empty_string_is_isogram() -> None:
#     isogram = is_isogram("")
#     assert isogram
#
#
# def test_is_isogram_false() -> None:
#     isogram = is_isogram("hello world")
#     assert not isogram
#
#
# def test_is_isogram_true() -> None:
#     isogram = is_isogram("bartek")
#     assert isogram
#
#
# def test_non_consecutive_letters_are_not_isogram() -> None:
#     isogram = is_isogram("pytest")
#     assert not isogram
#
#
# def test_consecutive_letters_are_isogram() -> None:
#     isogram = is_isogram("hello")
#     assert not isogram
