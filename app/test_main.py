from app.main import is_isogram


def test_should_return_true_for_empty_string() -> None:
    word = ""
    checking_string = is_isogram(word)
    if word == "":
        assert checking_string is True


def test_should_return_false_for_diff_cases_for_same_letter() -> None:
    word = "Ww"
    checking_string = is_isogram(word)
    assert checking_string is False


def test_should_return_false_if_more_than_one_same_letter() -> None:
    word = "Wow"
    checking_string = is_isogram(word)
    assert checking_string is False


def test_should_return_true_if_the_string_from_the_one_letter() -> None:
    word = "W"
    checking_string = is_isogram(word)
    assert checking_string is True


def test_should_return_true_if_the_string_consist_of_unique_letters() -> None:
    word = "Zander"
    checking_string = is_isogram(word)
    assert checking_string is True


def test_should_return_true_if_the_string_has_spaces() -> None:
    word = "No fate"
    checking_string = is_isogram(word)
    assert checking_string is True


def test_should_return_true_if_the_string_has_special_simbols() -> None:
    word = "Net@#_!$%&"
    checking_string = is_isogram(word)
    assert checking_string is True


def test_should_return_false_for_same_letters_with_spaces_and_simbols() \
        -> None:
    word = "a G g *@^#  m j m"
    checking_string = is_isogram(word)
    assert checking_string is False
