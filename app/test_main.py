from app.main import is_isogram


class TestIsIsogram:

    def test_playgrounds(self) -> None:
        assert is_isogram("playgrounds") is True

    def test_look(self) -> None:
        assert is_isogram("look") is False

    def test_adam(self) -> None:
        assert is_isogram("Adam") is False

    def test_quarters(self) -> None:
        assert is_isogram("") is True
