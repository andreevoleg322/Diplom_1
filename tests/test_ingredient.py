import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ("начинка", "Сыр", 200),
            ("соус", "Кетчуп", 100),
            ("начинка", "Говядина", 300),
            ("соус", "Горчичный", 50),
        ],
    )
    def test_init_and_getters(self, ingredient_type, name, price):

        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_get_price(self):

        ingredient = Ingredient("начинка", "Сыр", 200)

        assert ingredient.get_price() == 200

    def test_get_name(self):

        ingredient = Ingredient("начинка", "Сыр", 200)

        assert ingredient.get_name() == "Сыр"

    def test_get_type(self):

        ingredient = Ingredient("начинка", "Сыр", 200)

        assert ingredient.get_type() == "начинка"