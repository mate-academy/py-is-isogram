from app.main import is_isogram


class TestLetter:
    def test_empty_string(self):
        assert is_isogram("") is True

    def test_isogram_string(self):
        assert is_isogram("playgrounds") is True

    def test_same_lower_upper_letter(self):
        assert is_isogram("Dad") is False

    def test_three_same_letter(self):
        assert is_isogram("Puppy") is False
