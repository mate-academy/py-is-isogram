import pytest

from app.main import is_isogram


def get_data() -> list:
    return [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]


def key_gen(get_data_key_gen: list) -> str:
    word, expected = get_data_key_gen
    return (f"If word is a {word}, "
            f"result will {expected}")


@pytest.mark.parametrize("get_data_test",
                         get_data(),
                         ids=key_gen)
def test_app(get_data_test: list) -> None:
    word, expected = get_data_test
    assert is_isogram(word) == expected
