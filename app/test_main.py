import pytest


from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_string,expected_result",
        [
            ("", True),
            ("look", False),
            ("Adam", False),
            ("playground", True)
        ],
        ids=[
            "test empty string",
            "test consecutive string",
            "test non-consecutive string",
            "test an isogram string"
        ]
    )
    def test_empty_string(self,
                          input_string: str,
                          expected_result: bool) -> None:
        assert is_isogram(input_string) == expected_result
