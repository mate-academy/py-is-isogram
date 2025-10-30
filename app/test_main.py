import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [   # typical True variant
            pytest.param("lamp", True, id="unique lowercase letters"),
            pytest.param("bird", True, id="unique letters 2"),
            pytest.param("quiz", True, id="unique letters 3"),

            # one symbol and empty string
            pytest.param("", True, id="empty string"),
            pytest.param(" ", True, id="single space"),
            pytest.param("a", True, id="single character"),

            # typical False variant
            pytest.param("Alphabet", False, id="case-insensitive "
                                               "duplicate (A & a)"),
            pytest.param("banana", False, id="repeated letter separated"),
            pytest.param("letter", False, id="duplicate adjacent letters"),
            pytest.param("moOse", False, id="mixed case duplicate (O & o)"),

            # Non-typical variants
            pytest.param("six-year-old", False, id="hyphen makes repeat "
                                                   "of alphabet chars ignored "
                                                   "but hyphen repeated?"),
            pytest.param("ice man ", False,
                         id="space repeated — current behavior"),
            pytest.param("ice man", True,
                         id="space repeated — current behavior"),
            pytest.param("abc123", True, id="alphanumeric is isogram"),
            pytest.param("a1a", False, id="duplicate letter in alphanumeric"),
        ]
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
