from app.main import is_isogram


def test_empty_string_is_isogram():
    assert is_isogram("") is True, ("Empty string is an isogram")


def test_should_be_case_insensitive():
    words = ("bool", "coOl", "Alarm", "bosS")
    for word in words:
        assert is_isogram(word) is False, ("Word should be case insensitive.")


def test_should_equal_right_result():
    words = ("Azov", "sound", "playground", "abcdefg", "ёпрст")
    for word in words:
        assert is_isogram(word) is True
