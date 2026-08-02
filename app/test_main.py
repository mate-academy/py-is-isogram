from app.main import is_isogram


def test_return_true_for_isogram() -> None:
    goal = is_isogram("playgrounds")
    assert goal is True


def test_return_false_for_noisogram_with_uppercase() -> None:
    goal = is_isogram("Adam")
    assert goal is False


def test_return_true_for_empty_string() -> None:
    goal = is_isogram("")
    assert goal is True


def test_return_false_for_isogram_with_uppercase() -> None:
    goal = is_isogram("Playgrounds")
    assert goal is True


def test_return_false_for_noisogram() -> None:
    goal = is_isogram("daam")
    assert goal is False
