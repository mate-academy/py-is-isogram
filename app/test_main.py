import pytest


from app.main import is_isogram


class TestIsogram:
    @pytest.mark.paramitze(
        "izo_string, result",
        [
            pytest.param("Hania", True),
            pytest.param("Mateusz", True),
            pytest.param("Mom", False),
            pytest.param("", True),
            pytest.param("1Mat2eusz", False),
            pytest.param("1Mat2eusz", False),
            pytest.param("daD", False),
        ]
    )
    def test_for_isogram(
            self,
            izo_string: str,
            result: bool
    ) -> None:
        wyn = is_isogram(izo_string)
        assert wyn == result
