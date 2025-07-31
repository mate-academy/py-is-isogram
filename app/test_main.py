from app.main import is_isogram


class TestIsIsogram:
    def test_empty_string(self) -> None:
        assert is_isogram("") is True

    def test_single_character(self) -> None:
        assert is_isogram("a") is True
        assert is_isogram("b") is True

    def test_isogram(self) -> None:
        assert is_isogram("word") is True
        assert is_isogram("isogram") is True

    def test_not_isogram(self) -> None:
        assert is_isogram("hello") is False
        assert is_isogram("test") is False

    def test_mixed_case(self) -> None:
        assert is_isogram("Isogram") is True
        assert is_isogram("Hello") is False
        assert is_isogram("Test") is False
