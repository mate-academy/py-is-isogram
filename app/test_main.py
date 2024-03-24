from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "str_to_add, expected_bool",
        [
            (pytest.param("playgrounds", True, id="add of isolate is True")),
            (pytest.param("look", False, id="add of isolate is False")),
            (pytest.param("Adam", False, id="add of isolate with upper case")),
            (pytest.param("", True, id="empty string check"))
        ])
    def test_isogram(self, str_to_add: str, expected_bool: bool) -> None:
        assert is_isogram(str_to_add) == expected_bool
