from app.main import is_isogram


def test_empty_string_is_isogram():
    assert is_isogram("") is True


def test_spaced_string_is_isogram():
    assert is_isogram(" ") is True


def test_isogram_should_return_true():
    assert is_isogram("hydromagnetic") is True
    assert is_isogram("unforgivable") is True
    assert is_isogram("lexicography") is True
    assert is_isogram("backgrounds") is True
    assert is_isogram("facetiously") is True
    assert is_isogram("playgrounds") is True


def test_not_isogram_should_return_false():
    assert is_isogram("cowboy") is False
    assert is_isogram("werewolf") is False
    assert is_isogram("genshin") is False
    assert is_isogram("sunshine") is False
    assert is_isogram("purposefulness") is False
    assert is_isogram("excellent") is False


def test_upper_and_lower_case_is_same_letter():
    assert is_isogram("Cancer") is False
    assert is_isogram("Limboly") is False
    assert is_isogram("Repr") is False
    assert is_isogram("Sovest") is False
