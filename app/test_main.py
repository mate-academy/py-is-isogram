import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "world, result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("Olala", False)
        ]
    )
    def test_different_world(self, world, result):
        assert is_isogram(world) == result

    def test_not_world(self):
        try:
            assert is_isogram(1123)
        except AttributeError:
            print("You can't pass a number to a function")
