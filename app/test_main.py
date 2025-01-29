from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("Dermatoglyphics") is True, "Dermatoglyphics " \
        "is an isogram"
    assert is_isogram("aba") is False, "aba is not an isogram"
    assert is_isogram("moOse") is False, "moOse is not an isogram"
    assert is_isogram("thumbscrew-japingly") is True, "thumbscrew-japingly " \
        "is an isogram"
    assert is_isogram("") is True, "An empty string is an isogram"
    assert is_isogram("playgrounds") is True, "playgrounds is an isogram"
    assert is_isogram("look") is False, "look is not an isogram"
    assert is_isogram("Adam") is False, "Adam is not an isogram"
    assert is_isogram("") is True, "An empty string is an isogram"
