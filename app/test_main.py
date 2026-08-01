from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    """
    Тест для пустой строки. Пустая строка считается изограммой.
    """
    assert is_isogram("") is True


def test_is_isogram_single_character() -> None:
    """
    Строка из одного символа всегда является изограммой.
    """
    assert is_isogram("a") is True
    assert is_isogram("A") is True


def test_is_isogram_all_unique_characters() -> None:
    """
    Тест для строки, в которой все символы уникальны.
    """
    assert is_isogram("playgrounds") is True
    assert is_isogram("Dermatoglyphics") is True


def test_is_isogram_repeating_characters() -> None:
    """
    Тест для строки с повторяющимися символами.
    """
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("banana") is False


def test_is_isogram_case_insensitive() -> None:
    """
    Тест для проверки нечувствительности к регистру.
    """
    assert is_isogram("Isogram") is True
    assert is_isogram("IsOgRaM") is True
    assert is_isogram("Isogramm") is False


def test_is_isogram_non_letter_characters() -> None:
    """
    Тест для строки, содержащей небуквенные символы.
    Ожидается, что функция выбросит исключение ValueError.
    """
    assert is_isogram("123") is True
    assert is_isogram("abc123") is True
