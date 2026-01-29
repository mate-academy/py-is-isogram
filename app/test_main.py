import pytest
from app.main import is_isogram


@pytest.mark.parametrize("line", [""])
def test_line_len(line: str) -> None:
    assert is_isogram(line)
