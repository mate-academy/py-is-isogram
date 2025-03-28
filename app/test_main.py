from pytest import mark, param

from app.main import is_isogram


@mark.parametrize(
    "word,expected_result",
    [
        param("playgrounds", True,
              id="should return Trues when isogram"),
        param("look", False,
              id="should return False when duplicate letter"),
        param("Adam", False,
              id="should return False when capitalized duplicate"),
        param("", True,
              id="should return Trues when no empty str"),
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
