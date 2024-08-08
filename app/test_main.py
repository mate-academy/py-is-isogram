from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds"), "Test case 1 failed"
    assert not is_isogram("look"), "Test case 2 failed"
    assert not is_isogram("Adam"), "Test case 3 failed"
    assert is_isogram(""), "Test case 4 failed"
    assert is_isogram("isogram"), "Test case 5 failed"
    assert not is_isogram("GeeksforGeeks"), "Test case 6 failed"
    assert not is_isogram("Alphabet"), "Test case 7 failed"
    assert is_isogram("Dermatoglyphics"), "Test case 8 failed"
