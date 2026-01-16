from app.main import is_isogram
import pytest


@pytest.mark.parametrize("cat_year, result", [("playgrounds", True),
                                              ("look", False),
                                              ("Adam", False),
                                              ("", True)])
def test_cheking_values(cat_year: int,
                        result: list) -> None:

    assert (is_isogram(cat_year) == result), \
        "Somothing wrong with cat calculate:"
