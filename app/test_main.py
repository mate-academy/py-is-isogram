import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "", True,
                id="should return 'True' when input is empty string"),
            pytest.param(
                "playgrounds", True,
                id="should return 'True' when input is isogram word"),
            pytest.param(
                "look", False,
                id="should return 'False' when input is not isogram word"),
            pytest.param(
                "Adam", False,
                id="should return 'False' when input"
                   " is not isogram word with uppercase letters"),
            pytest.param(
                "234", True,
                id="should return 'True' when input is string number isogram"),
            pytest.param(
                "2342", False,
                id="should return 'False' when "
                   "input is not string number isogram"),
            pytest.param(
                "PlAyGrOuNdS", True,
                id="should return 'False' when input"
                   " is isogram word with uppercase letters"),
            pytest.param(
                "pale+123", True,
                id="should return 'True' when input"
                   " is isogram with special symbols"),
        ]
    )
    def test_is_isogram_working_correctly(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
