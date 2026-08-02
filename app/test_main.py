from app.main import is_isogram


def test_should_return_true_for_empty() -> None:
    assert is_isogram("")


def test_should_return_true_for_isogram_with_upper() -> None:
    assert is_isogram("PlaYgrounds")


def test_should_return_false() -> None:
    assert not is_isogram("Adam")


def test_should_return_false_for_non_consecutive() -> None:
    assert not is_isogram("look")
