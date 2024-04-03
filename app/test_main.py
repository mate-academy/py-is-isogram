import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "given_word, expected_result",
    [
        pytest.param("playgrounds", True,
                     id="expecting True when each letter is unique"),
        pytest.param("look", False,
                     id="expecting False if there are same letters"),
        pytest.param("Adam", False,
                     id="expecting False if there are same letters."
                        "letters are case-insensitive"),
        pytest.param("", True,
                     id="expecting True as empty string"),
    ]
)
def test_correct_count(
        given_word: str,
        expected_result: bool
) -> None:
    assert is_isogram(given_word) == expected_result
