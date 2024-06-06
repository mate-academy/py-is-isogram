from app.main import is_isogram


def test_is_isogram() -> None:
    assert (
        is_isogram("playgrounds") is True
    )


def test_is_isogran_empty() -> None:
    assert (
        is_isogram("") is True
    )


def test_is_isogram_consecutive() -> None:
    test_cases = [
        "look",
        "Adam",
        "boRow",
        "leleka"
    ]
    for case in test_cases:
        isogram_case = is_isogram(case)

        assert isogram_case is False
