import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "isogram, check",
        [
            pytest.param(
                "",
                True,
                id="should return true for empty string"
            ),
            pytest.param(
                "aa",
                False,
                id="should return false for consecutive repeats"
            ),
            pytest.param(
                "cascade",
                False,
                id="should return false if letters are not consecutive"
            ),
            pytest.param(
                "Aaron",
                False,
                id="should return false if cases are different"
            ),
        ]
    )
    def test_is_isogram(self,
                        isogram,
                        check):
        assert is_isogram(isogram) is check
