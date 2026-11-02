from app import main


def test_main():
    assert main.is_isogram("Adam") is False
    assert  main.is_isogram("Lord") is True
    assert main.is_isogram("") is True
    assert main.is_isogram("playgrounds") is True
    assert main.is_isogram("aba") is False
