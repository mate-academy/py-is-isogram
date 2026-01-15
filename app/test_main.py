from app.main import is_isogram
import pytest


class TestIsIsogram:
    def test_positive_case(self) -> None:
        assert is_isogram("abc") is True

    def test_case_insensitive(self) -> None:
        assert is_isogram("Bob") is False

    def test_empty_string(self) -> None:
        assert is_isogram("") is True

    def test_lange_string(self) -> None:
        assert is_isogram("abcdefghijklmnoprstuvwxyz") is True

    def test_number_string(self) -> None:
        assert is_isogram("0123456789") is True

    def test_invalid_type(self) -> None:
        with pytest.raises(Exception):
            is_isogram(1234)
