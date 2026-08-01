from typing import Any


import pytest


from app.main import is_isogram


class TestError:
    @pytest.mark.parametrize("word", [
        pytest.param(12, id="should raise"
                            " an error while int"),
        pytest.param(True, id="should raise"
                              " an error while bool"),
        pytest.param(None, id="should raise"
                              " an error while None"),
        pytest.param(11.3, id="should raise"
                              " an error while float"),
        pytest.param(["word"], id="should raise"
                                  " an error while list"),
        pytest.param({"word"}, id="should raise"
                                  " an error while set"),
        pytest.param({"word": "letter"}, id="should raise"
                                            " an error while dict"),
        pytest.param(("new word", ), id="should raise"
                                        " an error while tuple"),
    ])
    def test_should_raise_error_when_incorrect(self, word: Any) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)


class TestValidOutput:
    @pytest.mark.parametrize("word, result", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("MADAM", False),
        ("andrew", True),
        ("acrobAt", False),
        ("qwertyasdf", True),
        ("123password", False)
    ])
    def test_should_return_correct_result(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result
