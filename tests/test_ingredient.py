import pytest
from praktikum.ingredient_types import *
from praktikum.ingredient import *


class TestIngredient:

    @pytest.mark.parametrize('price', [-100, -0.1, 0, 0.1, 100])
    def test_ingredient_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'name', price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', ['', 'Lorem ipsum dolor sit amet, consectetuer '])
    def test_ingredient_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_ingredient_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'name', 100)
        assert ingredient.get_type() == ingredient_type
