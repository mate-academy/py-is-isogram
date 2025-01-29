import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "value,expected_result",
        [
            ("", True),
            ("playgrounds", True),
            ("look", False),
            ("Hello", False),
            ("StRiKe", True),
            ("FoOtbalL", False),
            ("nfrikngwri", False),
            ("mowvjnqp", True)
        ]
    )
    def test_isogram(
            self,
            value: str,
            expected_result: bool,
    ) -> None:
        assert is_isogram(value) == expected_result
