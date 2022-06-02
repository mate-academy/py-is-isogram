from app.main import is_isogram


class TestIsIsogram:
    def test_string_is_empty_should_be_true(self):
        goals = is_isogram("")
        assert goals is True

    def test_not_isogram_should_be_false(self):
        goals = is_isogram("look")
        assert goals is False

    def test_not_isogram_string_with_uppercase(self):
        goals = is_isogram("Adam")
        assert goals is False

    def test_isogram_should_be_true(self):
        goals = is_isogram("playgrounds")
        assert goals is True

    def test_isogram_with_uppercase(self):
        goals = is_isogram("AdOlF")
        assert goals is True

    def test_isogram_with_uppercase_and_not_isog(self):
        goals = is_isogram("Madam")
        assert goals is False
