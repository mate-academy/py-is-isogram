import pytest
from app.main import is_isogram


@pytest.mark.parametrize("line, expected_answer",
        [                
            ['', True]                
                                     
        ])

def test_line_len(line: str, expected_answer: bool) -> None:
    assert len(line) == 0
