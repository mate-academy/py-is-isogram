from app.main import is_isogram


def test_empty_string():
    assert is_isogram("")


def test_true():
    values = ["unCopyrIghtAbLe", "aMbiDextrOuslY", "plaYGrounDs"]
    actual = []
    for word in values:
        actual.append(is_isogram(word))

    assert all(actual)


def test_false():
    values = ["loOk", "Adam", "DOcToRwHO"]
    actual = []
    for word in values:
        actual.append(is_isogram(word))

    assert not all(actual)


def test_symbols():
    assert not is_isogram('**8+%+9865)')
    assert is_isogram('*8%+965)')
