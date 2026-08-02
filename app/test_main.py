from app.main import is_isogram


def test_empty_input():
    assert is_isogram("") is True


def test_low_and_capital_letters():
    assert is_isogram("moM") is False
