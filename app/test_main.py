from app.main import is_isogram


def test_should_return_true_when_world_empty() -> None:
    assert is_isogram("") is True


def test_should_return_true_when_world_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_when_world_not_isogram() -> None:
    assert is_isogram("Adam") is False
