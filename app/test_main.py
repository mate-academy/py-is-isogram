from app.main import is_isogram


class TestIsogram:
    def test_empty_string(self):
        assert is_isogram('') is True

    def test_isogram_string(self):
        assert is_isogram('playgrounds') is True

    def test_repeat_letter(self):
        assert is_isogram('Adam') is False

    def test_repeat_upper_and_low_letters(self):
        assert is_isogram('look') is False
