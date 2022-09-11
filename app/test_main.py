from app.main import is_isogram


class TestIsIsogram:
    def test_empty_string(self):
        assert is_isogram("") is True

    def test_word_is_isogram(self):
        assert is_isogram("playgrounds") is True

    def test_word_isnt_isogram(self):
        assert is_isogram("look") is False

    def test_should_be_case_intensive(self):
        assert is_isogram("Adam") is False
