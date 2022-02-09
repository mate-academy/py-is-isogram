from app.main import is_isogram


def test_empty_string_and_result_type_bool():
    assert is_isogram("") is True


def test_repeated_insensitive_letters():
    assert is_isogram("feEt") is False
    assert is_isogram("bAnAna") is False


def test_caseinsensitive_and_no_repeated_letters():
    assert is_isogram("uncOpyrightAble") is True
    assert is_isogram("copyrightable") is True


def test_repeated_letters():
    assert is_isogram("ololo") is False
    assert is_isogram("foo") is False
