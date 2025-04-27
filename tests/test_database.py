import pytest
from unittest.mock import Mock, patch
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient



class TestDatabase:

    def test_init(self):

        db = Database()

        assert len(db.buns) == 3
        assert len(db.ingredients) == 6
        assert all(isinstance(bun, Bun) for bun in db.buns)
        assert all(isinstance(ingredient, Ingredient) for ingredient in db.ingredients)

    def test_available_buns(self):

        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns == db.buns

    def test_available_ingredients(self):

        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        assert ingredients == db.ingredients
