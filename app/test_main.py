from app.main import is_isogram


def test_is_isogram() -> None:
    test_data = [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]

    for word, result in test_data:
        assert is_isogram(word) == result
