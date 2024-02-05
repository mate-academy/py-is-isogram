from app.main import is_isogram


def test_return_the_empty_string_true():
    assert is_isogram("")


def test_M_and_m_are_considered_the_same_letter():
    assert not is_isogram("Adam")


def test_ead_to_the_repetition_of_letters():
    assert not is_isogram("look")

def test_should_is_an_isogram():
    assert is_isogram("playgrounds")