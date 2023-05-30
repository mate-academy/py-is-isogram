import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("l", True),
        ("dialogue", True),
        ("DEpth", True),
        ("deed", False),
        ("xslfxlfs", False),
        ("DeEd", False)

    ],
    ids=[
        "Should work with empty string",
        "Should work with one symbol",
        "Should work with First-Order isogram",
        "Should work with lower and upper case text",
        "Shouldn`t work with Second and more order isogram",
        "Shouldn`t work with not consecutive symbols",
        "Shouldn`t work with same symbols with different cases"
    ]
)
def test_should_work_correct(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), "Function should work correctly"
