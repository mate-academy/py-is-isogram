from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, bool_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Fg7K", True),
        ("1234", True),
        ("asd?fgh", True),
        ("?asdF?+*-'7()", False)
    ]
)
def test_is_isogram(word: str,
                    bool_result: bool
                    ) -> bool:
    assert is_isogram(word) == bool_result
