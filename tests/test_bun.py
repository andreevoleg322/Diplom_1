import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("Краторная булка", 1000),
            ("Флюоресцентная булка", 2000),
            ("", 0),
            ("Специальная булка", -1),
        ],
    )
    def test_init_and_getters(self, name, price):

        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_get_name_mocked(self):

        mock_bun = Mock()
        mock_bun.get_name.return_value = "Какая-то булка"

        assert mock_bun.get_name() == "Какая-то булка"

    def test_get_price_mocked(self):

        mock_bun = Mock()
        mock_bun.get_price.return_value = 1

        assert mock_bun.get_price() == 1