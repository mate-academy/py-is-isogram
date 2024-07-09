from app.main import is_isogram
import pytest


class TestIsHistogram:
    @pytest.mark.parametrize(
        "input_str, result_bool", [
            ("rectangle", False),
            ("Atom", True),
            ("playgrounds", True),
            ("ambidextrously", True),
            ("Outlook", False),
            ("", True),
            ("Alphabet", False)
        ]
    )
    def test(self, input_str: str, result_bool: bool) -> None:
        assert is_isogram(input_str) == result_bool
