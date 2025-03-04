from app.main import is_isogram


def test_is_isogram() -> None:
    # Тест для порожнього рядка
    assert is_isogram("") is True

    # Тести для слів без повторюваних літер (ізограми)
    assert is_isogram("playgrounds") is True
    assert is_isogram("uncopyrightable") is True  # Довге слово без повторень

    # Тести для слів з повторюваними літерами
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False  # Перевірка чутливості до регістру
    assert is_isogram("letter") is False

    # Перевірка змішаних регістрів
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("MoOse") is False
    # "o" повторюється, незалежно від регістру
