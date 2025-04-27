import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_init(self):

        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):

        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Черная булка"
        mock_bun.get_price.return_value = 999

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self):

        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "Колбаса"
        mock_ingredient.get_price.return_value = 1

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):

        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.ingredients = [mock_ingredient]

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):

        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        burger.ingredients = [mock_ingredient1, mock_ingredient2]

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_price",
        [
            (1000, [200, 300], 2500),
            (500, [100, 150], 1250),
            (0, [], 0),
        ],
    )
    def test_get_price(self, bun_price, ingredient_prices, expected_price):

        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_price
