import pytest

from app.main import is_isogram


class TestMain:
    @pytest.mark.parametrize(
        "text,bool_value",
        [
            pytest.param("Misha", True),
            pytest.param("Yana", False),
            pytest.param("asdfghjk", True),
            pytest.param("", True),
            pytest.param("Daddy", False),
            pytest.param("Aa", False)
        ]
    )
    def test_func(self,
                  text: str,
                  bool_value: bool) -> None:
        assert is_isogram(text) == bool_value
