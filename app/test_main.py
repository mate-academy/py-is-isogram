import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word,boolean",
    [
        pytest.param(
            "", True,
            id="empty string should return True"
        ),
        pytest.param(
            "abc", True,
            id="isogram should return True"
        ),
        pytest.param(
            "abca", False,
            id="NOT isogram should return False"
        ),
        pytest.param(
            "ABca", False,
            id="upper case should count like lower case"
        )
    ]
)
def test_is_isogram_work_correctly(word: str, boolean: bool) -> None:
    assert is_isogram(word) == boolean
