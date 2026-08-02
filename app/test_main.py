import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True,
                     id="should return 'True' when word is isogram"),
        pytest.param("look", False,
                     id="should return 'False' "
                        "when sting have 2 identical characters"),
        pytest.param("Adam", False,
                     id="should return 'False' "
                        "despite the case of identical letters"),
        pytest.param("", True,
                     id="should return 'True' if word is empty string")

    ]
)
def test_correct_value(word: str, result: bool) -> None:

    assert is_isogram(word) == result
