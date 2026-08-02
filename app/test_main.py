from app.main import is_isogram


def test_pusty_ciag() -> None:
    assert is_isogram("")


def test_pojedyncza_litera() -> None:
    assert is_isogram("a")


def test_wszystkie_unikalne_litery() -> None:
    assert is_isogram("playgrounds")


def test_powtarzające_się_litery() -> None:
    assert not is_isogram("look")


def test_niewrażliwość_na_wielkość_liter() -> None:
    assert not is_isogram("Adam")


def test_mieszane_wielkości() -> None:
    assert not is_isogram("Alphabet")


def test_ze_spacjami() -> None:
    assert not is_isogram("No Spaces")


def test_znaki_specjalne() -> None:
    assert not is_isogram("Hello!")
