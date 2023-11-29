import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "enter_word,result",
        [
            pytest.param("", True, id="test empty string"),
            pytest.param("coLizeum", True, id="test isogram with different cases"),
            pytest.param("coLlizeum", False, id="test different cases of same letter"),
            pytest.param("morning", False, id="test whether not isogram is not isogram"),
            pytest.param("dragon", True, id="test whether isogram is isogram")
        ]
    )
    def test_is_repetting_letters(
            self,
            enter_word: str,
            result: bool
    ) -> None:

        assert is_isogram(enter_word) == result
