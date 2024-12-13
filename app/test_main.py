from app.main import is_isogram


def test_that_big_letter_eaquel_to_small_letter() -> None:
    assert is_isogram("AbC") is True
    assert is_isogram("AbCAbC") is False
