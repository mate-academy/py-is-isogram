from app.main import is_isogram


def test_isogram_true() -> None:
    assert is_isogram("playgrounds") is True
