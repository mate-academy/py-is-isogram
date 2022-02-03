from app.main import is_isogram


def test_for_empty_string():
    assert is_isogram("") is True


def test_case_insensitivity():
    assert is_isogram("pReTtY") == is_isogram("PrEtTy")


def test_repeated_letters():
    assert is_isogram("ihavealotrepeatedletter") is False
