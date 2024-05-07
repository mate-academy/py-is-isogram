from app.main import is_isogram
import pytest


class TestData:
    @pytest.mark.parametrize(
        "data_init, expected_data",
        [
            pytest.param(
                "playgrounds",
                True,
                id="Test playgrounds"
            ),
            pytest.param(
                "",
                True,
                id="Test empty"
            ),
            pytest.param(
                "3434",
                False,
                id="Test number"
            ),
            pytest.param(
                "Ada",
                False,
                id="Test Case"
            ),
            pytest.param(
                "zoom",
                False,
                id="Test zoom"
            ),


        ]

    )
    def test_isograph(self,
                      data_init: str,
                      expected_data: bool
                      ) -> None:
        assert is_isogram(data_init) == expected_data
