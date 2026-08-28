import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "",
            True,
            id="check empty str"
        ),
        pytest.param(
            "Hi",
            True,
            id="check: Hi"
        ),
        pytest.param(
            "Hello",
            False,
            id="check: Hello"
        ),
        pytest.param(
            "lol",
            False,
            id="check: lol"
        ),
        pytest.param(
            "Asap",
            False,
            id="check: Asap"
        ),
        pytest.param(
            "SEE",
            False,
            id="check: SEE"
        ),
        pytest.param(
            "BOB",
            False,
            id="check: BOB"
        ),
        pytest.param(
            "OPPOSITE",
            False,
            id="check: OPPOSITE"
        ),
        pytest.param(
            "QWERTYUIOPASDFGHJKLZXCVBNM",
            True,
            id="check: every word in uppercase"
        ),
        pytest.param(
            "qwertyuiopasdfghjklzxcvbnm",
            True,
            id="check: every word in lowercase"
        ),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
