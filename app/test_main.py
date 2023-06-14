import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_bool",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("lOok", False),
        ("Adam", False),
        ("success", False),
        ("SucCeSs", False),
        ("niGga", False),
        ("uncopyrightables", True),
        ("unpredictably", True)
    ],
    ids=[
        "empty string should return `True`",
        "`playgrounds` should return `True`",
        "`look` should return `False`",
        "`lOok` should return `False`",
        "`Adam` should return `False`",
        "`success` should return `False`",
        "`SucCeSs` should return `False`",
        "`niGga` should return `False`",
        "`uncopyrightables` should return `True`",
        "`unpredictably` should return `True`"
    ]
)
def test_checks_isograms_correctly(word: str, expected_bool: bool) -> None:
    assert is_isogram(word) == expected_bool
