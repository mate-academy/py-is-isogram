import pytest

from app.main import is_isogram


class TestIsogram:

    @pytest.mark.parametrize("world, returned", [
        pytest.param('playgrounds', True, id="True isogram test"),
        pytest.param('look', False, id="False isogram test"),
        pytest.param("", True, id="Empty string test")
    ])
    def test_is_isogram(self, world: str, returned: bool) -> None:
        assert is_isogram(world) == returned
