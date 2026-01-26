import pytest
from app import main


@pytest.mark.parametrize(
    "word",
    [
        (6),
        (["Hello"]),
        (("word", "Hello")),
        (3.45),
        (True),
        ({"word": "Hello"}),
    ],
)
def test_data_input_is_a_string(
    word: str,
) -> None:
    with pytest.raises(TypeError):
        main.is_isogram(word)


@pytest.mark.parametrize(
    "word",
    [
        "345",
        "h3llo",
        "Hello World",
        "patet¡c",
        "$urprise",
    ],
)
def test_word_must_to_be_alpha(
    word: str,
) -> None:
    with pytest.raises(ValueError):
        main.is_isogram(word)


@pytest.mark.parametrize(
    "word",
    [
        "Thirty",
        "hello",
        "HelloWorld",
        "patetic",
        "surprise",
    ],
)
def test_function_return_must_to_be_bool(word: str) -> None:
    response = main.is_isogram(word)
    assert type(response) is bool, f"Return {response} must to be bool"


@pytest.mark.parametrize(
    "word, result",
    [
        ("Thirty", False),
        ("hello", False),
        ("open", True),
        ("close", True),
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ],
)
def test_function_is_isogram(word: str, result: bool) -> None:
    assert main.is_isogram(word) == result, f"Word {word} must return {result}"
