import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("Lemon", True),
            ("Wind", True),
            ("Sign", True),
            ("Badger", True),
            ("AbCdEfG", True)
        ]
    )
    def test_is_isogram(
            self,
            test_input: str,
            expected: bool) -> None:
        assert is_isogram(test_input) == expected

    def test_is_isogram_empty(self):
        assert is_isogram(" ") == True

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("Moose", False),
            ("AAasdweA", False),
            ("qweee", False),
            ("   ", False),
            ("Phantam", False)
        ]
    )
    def test_is_isogram_false(
            self,
            test_input: str,
            expected: bool) -> None:
        assert is_isogram(test_input) == expected

