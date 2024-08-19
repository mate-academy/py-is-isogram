from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ('', True),
    ('a', True),
    ('playgrounds', True),
    ('look', False),
    ('Adam', False),
    ('Python', True),
    ('Letter', False),
    ('aaaaa', False),
    ('aba', False)
])
def test_isogram(word: str, expected: list[str]) -> None:
    assert is_isogram(word) == expected
