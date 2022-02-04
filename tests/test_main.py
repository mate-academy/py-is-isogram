from app.main import is_isogram


def test_empty_string_and_result_type_bool():
    assert is_isogram("") == True


def test_for_upper_case_letters_and_isograms():
    assert is_isogram("Apex") == True
    assert is_isogram("FulL") == False
    assert is_isogram("bAnaNA") == False
    assert is_isogram("dermatoglyphics") == True
