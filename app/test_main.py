import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("a", True),
        ("word", True),
        ("kraken", False),
        ("WoRd", True),
        ("WATER", True),
        ("", True),
        (" ", True),
        ("Jake", True),
        ("Anna", False),
        ("cupcake", False),
        ("haPpy", False),
    ],
    ids=[
        "Is word `a` an isogram",
        "Is word `word` an isogram",
        "Is word `kraken` an isogram",
        "Is word `WoRd` an isogram",
        "Is word `WATER` an isogram",
        "Is empty string an isogram",
        "Is space and isogram",
        "Is word `Jake` an isogram",
        "Is word `Anna` an isogram",
        "Is word `cupcake` an isogram",
        "Is word `haPpy` an isogram",
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
