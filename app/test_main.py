from app.main import is_isogram


def test_should_return_true():
    assert is_isogram('playgrounds')


def test_should_return_true2():
    assert is_isogram('')


def test_should_return_false():
    assert not is_isogram('look')


def test_should_return_false2():
    assert not is_isogram('Adam')
