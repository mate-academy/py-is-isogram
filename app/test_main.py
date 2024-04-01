import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("", True),
            (" ", True),
            ("  ", False),
            ("abc", True),
            ("DFG", True),
            ("UTFu", False),
            ("Abracadabra", False),
            ("abcdefghijklmnopqrstuvwxyz", True)
        ]
    )
    def test_possible_often_used_cases(
            self,
            word: str,
            expected: bool) -> None:

        assert is_isogram(word) == expected

    @pytest.mark.parametrize(
        "word, expected_error",
        [
            (1, AttributeError),
            (True, AttributeError),
            ([1], AttributeError),
            ({}, AttributeError),
            (None, AttributeError)
        ]
    )
    def test_should_raise_error_when_wrong_type_provided(
            self,
            word: str,
            expected_error: type[Exception]) -> None:

        with pytest.raises(expected_error):
            is_isogram(word)
