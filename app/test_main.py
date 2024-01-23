import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "", True,
            id="should return True if word is an empty string"
        ),
        pytest.param(
            "isogram", True,
            id="should return True when word has no repeating letters"
        ),
        pytest.param(
            "pytest", False,
            id="should return False when word has repeating letters"
        ),
        pytest.param(
            "TerMinaL", True,
            id="should return True when word \
                has different case and no repeating letters"
        ),
        pytest.param(
            "SenSitIve", False,
            id="should return False when word \
                has different case and repeating letters"
        ),
        pytest.param(
            "Look", False,
            id="should return False when word \
                has consecutive repeating letters"
        )
    ]
)
def test_returns_value_correctly(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result


@pytest.mark.parametrize(
    "word, expected_error",
    [
        pytest.param(
            123, AttributeError,
            id="should raise AttributeError when word's type is int"
        ),
        pytest.param(
            [3433], AttributeError,
            id="should raise AttributeError when word's type is list"
        ),
        pytest.param(
            {858855}, AttributeError,
            id="should raise AttributeError when word's type is set"
        ),
        pytest.param(
            (1234567), AttributeError,
            id="should raise AttributeError when word is tuple with number"
        ),
        pytest.param(
            {"567": 567}, AttributeError,
            id="should raise AttributeError when word's type is dict"
        )
    ]
)
def test_raises_exception_correctly(
    word: str,
    expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
