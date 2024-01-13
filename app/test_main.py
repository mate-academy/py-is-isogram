from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "sentence,true_or_false",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_for_the_correctness_of_the_definition_of_the_isogram(
        sentence: str,
        true_or_false: bool
) -> None:
    assert is_isogram(sentence) == true_or_false
