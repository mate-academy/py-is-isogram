import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "incoming_string, expected_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_is_isogram(
            self,
            incoming_string: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(incoming_string) == expected_result
