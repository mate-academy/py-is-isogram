import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    ("word", "result"),
    [
        pytest.param("playgrounds", True,
                     id="should return True"),
        pytest.param("look", False,
                     id="should return False"),
        pytest.param("Adam", False,
                     id="should consider upper and lower cases"),
        pytest.param("", True,
                     id="empty str should return True"),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
