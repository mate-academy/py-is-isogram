import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result", [
        ("", True),
        ("Mm", False),
        ("playground", True),
        ("movement", False)
    ]
)
def test_if_result_is_correct(
    word: str,
    result: bool
) -> None:
    assert is_isogram(word) == result, f"Result should be {result}"
