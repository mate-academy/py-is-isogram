from app import main


def test_isogram_is_case_insensitive() -> None:
    assert not main.is_isogram("hello"), "The word 'hello' is not an isogram."
    assert main.is_isogram("Dermatoglyphics"),\
        "The word 'Dermatoglyphics' is an isogram."
    assert main.is_isogram("isogram"), "The word 'isogram' is an isogram."
    assert not main.is_isogram("moOse"), "The word 'moOse' is not an isogram."
    assert main.is_isogram("thumbscrewjapingly"),\
        "The word 'thumbscrewjapingly' is an isogram."
    assert main.is_isogram(""), "Empty string is an isogram."


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert not main.is_isogram("banana"),\
        "The word 'banana' is not an isogram."
    assert not main.is_isogram("elephant"),\
        "The word 'elephant' is not an isogram."
    assert not main.is_isogram("moOse"),\
        "The word 'moOse' is not an isogram."
    assert not main.is_isogram("book"),\
        "The word 'book' is not an isogram."
