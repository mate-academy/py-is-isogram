from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    """Проверяет, что пустая строка считается изограммой."""
    assert is_isogram("") is True


def test_single_letter_is_isogram() -> None:
    """Проверяет, что строка из одной буквы — изограмма."""
    assert is_isogram("a") is True
    assert is_isogram("Z") is True


def test_unique_letters_is_isogram() -> None:
    """Проверяет, что строка с уникальными буквами — изограмма."""
    assert is_isogram("playgrounds") is True
    assert is_isogram("cat") is True
    assert is_isogram("xyz") is True


def test_repeating_letters_is_not_isogram() -> None:
    """Проверяет, что строка с повторяющимися буквами — не изограмма."""
    assert is_isogram("look") is False  # Две 'o'
    assert is_isogram("hello") is False  # Две 'l'
    assert is_isogram("book") is False   # Две 'o'


def test_case_insensitive_repeating_letters() -> None:
    """Проверяет, что повторяющиеся буквы в разном регистре делают строку не изограммой."""
    assert is_isogram("Adam") is False  # 'A' и 'a' — одна буква
    assert is_isogram("mOon") is False  # 'O' и 'o' — одна буква
    assert is_isogram("TeSt") is False   # 'T' и 't' — одна буква


def test_case_insensitive_unique_letters() -> None:
    """Проверяет, что уникальные буквы в разном регистре — изограмма."""
    assert is_isogram("Cat") is True    # C, a, t
    assert is_isogram("DoG") is True    # D, o, G
    assert is_isogram("PyThOn") is True # P, y, T, h, O, n

