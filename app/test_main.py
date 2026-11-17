import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, bool_result",
    [
        pytest.param("", True, id="Empty string is an Isogram."),
        pytest.param("Mam", False, id="Word with capital letters at the beginning."),
        pytest.param("A", True, id="A single capital letter is an Isogram."),
        pytest.param("a", True, id="A single letter is an isogram."),
        pytest.param("Ambiguos", True, id="Long Isogram."),
        pytest.param("True", True, id="True is an Isogram."),
        pytest.param("False", True, id="False is also an Isogram."),
        pytest.param("mum", False, id="mum is not an Isogram."),
        pytest.param("Isogram", True, id="Isogram is an Isogram."),
        pytest.param("Number", True, id="Number is an Isogram."),
        pytest.param("less", False, id="less is not an Isogram."),
        pytest.param("word", True, id="word is an Isogram."),
    ]
)
def test_is_isogram(word, bool_result):
    assert (is_isogram(word) == bool_result), f"Error with the word {word}."
