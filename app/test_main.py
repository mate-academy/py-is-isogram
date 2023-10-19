from app.main import is_isogram


class TestIsIsogram:
    def test_for_empty_string(self) -> None:
        assert is_isogram("")

    def test_start_with_uppercase(self) -> None:
        assert is_isogram("Daniel")

    def test_uppercase_inside_word(self) -> None:
        assert is_isogram("daNiel")

    def test_word_in_lowercase_not_isogram(self) -> None:
        assert not is_isogram("look")

    def test_word_with_uppercase_not_isogram(self) -> None:
        assert not is_isogram("Adam")
