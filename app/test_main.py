import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            ("alegro", True),
            ("allegro", False),
            ("1234567890", True),
            ("", True),
            ("abcdefghijklmnopqrstuvwxyz", True),
            ("ABCDEFGHIJKLMNOPQRSTUVWXYZ.", True),
            ("AlBert", True),
            ("DomInIKA", False),
            ("aLlegro", False),
        ],
        ids=[
            "Simple isogram, should return 'True'",
            "Simple non isogram, should return 'False'",
            "Digits only, no duplicates, should return 'True'",
            "Empty string, should return 'True'",
            "Big lowercase text, should return 'True'",
            "Big uppercase text, should return 'False'",
            "Case sensitive simple isogram, should return 'True'",
            "Case sensitive simple non isogram, should return 'False'",
            "String with different cases of the same letter is not an isogram"
        ]
    )
    def test_if_word_is_isogram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result


