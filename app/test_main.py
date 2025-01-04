import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param('playgrounds', True, id="Text should return True"),
        pytest.param('look', False, id="Text should return False"),
        pytest.param('Adam', False, id="The test checks the processing of capital letters"),
        pytest.param('', True, id="Text check empty str")
    ]
)
def test_should_check_return_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result

