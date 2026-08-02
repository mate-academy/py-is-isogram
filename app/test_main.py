from app.main import is_isogram


class TestCases:
    def test_case_insensitive_is_isogram(self) -> None:
        assert ((is_isogram("playgrounds") is True)
                and (is_isogram("PlaYgrOunDs") is True)), (
            "function should be case-insensitive"
        )

    def test_case_insensitive_non_isogram(self) -> None:
        assert ((is_isogram("Adam") is False)
                and (is_isogram("adAm") is False)), (
            "function should be case-insensitive and word is not isogram"
        )


def test_empty_string() -> None:
    assert is_isogram("") is True, "empty string is isogram"


def test_is_word_isogram() -> None:
    assert is_isogram("look") is False, "word shouldn't have duplicates"
