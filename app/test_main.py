from typing import Any

import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "text, answer",
    [
        pytest.param(
            "playgrounds",
            True,
            id=("is a word should be no repeating letters, "
                "consecutive or non-consecutive")
        ),
        pytest.param(
            "look",
            False,
            id=("is a word should be no repeating letters, "
                "consecutive or non-consecutive")
        ),
        pytest.param(
            "Adam",
            False,
            id=("is a word should be no repeating letters, "
                "consecutive or non-consecutive")
        ),
        pytest.param(
            "",
            True,
            id=("is a word should be no repeating letters, "
                "consecutive or non-consecutive")
        ),
    ]
)
def test_check_isogram(
        text: str,
        answer: bool
) -> None:
    assert is_isogram(text) == answer


@pytest.mark.parametrize(
    "text, error",
    [
        pytest.param(
            123,
            AttributeError,
            id="'int' object has no attribute 'lower'"
        ),
    ]
)
def test_raising_error(
        text: str,
        error: Any
) -> None:
    with pytest.raises(error):
        assert is_isogram(text)
