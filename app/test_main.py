from app.main import is_isogram


def test_with_empty_string():
    assert is_isogram("") is True


def test_with_real_isogram():
    assert is_isogram("playgrounds") is True


def test_isogram_with_mixed_case():
    assert is_isogram("PLAYgrounds") is True


def test_isogram_with_all_capital():
    assert is_isogram("PLAYGROUND") is True


def test_with_consecutive():
    assert is_isogram("APple") is False


def test_with_non_consecutive():
    assert is_isogram("AdaM") is False
