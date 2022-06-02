from app.main import is_isogram


class TestIsIsogram:
    def test_no_letters(self):
        assert is_isogram("") is True

    def test_one_letter(self):
        assert is_isogram("a") is True
        assert is_isogram("A") is True

    def test_uppercase(self):
        assert is_isogram("Aa") is False
        assert is_isogram("AA") is False

    def test_different_words(self):
        assert is_isogram('playgrounds') is True
        assert is_isogram('look') is False
