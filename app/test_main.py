from app.main import is_isogram


def test_empty_string() -> None:
    word = ""
    actually_result = is_isogram(word)
    expected = True
    assert actually_result is expected


def test_amaterasu_word() -> None:
    word = "amaterasu"
    actually_result = is_isogram(word)
    expected = False
    assert actually_result is expected


def test_isanagi_word() -> None:
    word = "isanagi"
    actually_result = is_isogram(word)
    expected = False
    assert actually_result is expected


def test_word_with_pascal_case() -> None:
    word = "Kotoamatsukami"
    actually_result = is_isogram(word)
    expected = False
    assert actually_result is expected


def test_kamui_word() -> None:
    word = "kamui"
    actually_result = is_isogram(word)
    expected = True
    assert actually_result is expected
