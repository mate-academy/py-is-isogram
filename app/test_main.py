from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("") is True
    assert is_isogram("hi") is True
    assert is_isogram("word") is True
    assert is_isogram("play") is True
    assert is_isogram("run") is True
    assert is_isogram("man") is True
    assert is_isogram("woman") is True
    assert is_isogram("python") is True
    assert is_isogram("ark") is True
    assert is_isogram("night") is True

    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("hell") is False
    assert is_isogram("Hello") is False
    assert is_isogram("test") is False
    assert is_isogram("Heroes") is False
    assert is_isogram("darkness") is False
    assert is_isogram("papa") is False
    assert is_isogram("mama") is False
    assert is_isogram("pip") is False
    assert is_isogram("digital") is False
