from app.main import is_isogram


class TestIsIsoGram:
    def test_string_is_empty(self) -> None:
        assert is_isogram("") == True

    def test_string_letter_meet_once(self) -> None:
        assert is_isogram("look") == False

    def test_string_letter_meet_twice(self) -> None:
        assert is_isogram("playgrounds") == True

    def test_string_letter_in_uppercase_meet_twice(self) -> None:
        assert is_isogram("Adam") == False