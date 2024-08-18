from praktikum.burger import *
from praktikum.ingredient import *
from praktikum.ingredient_types import *
from tests.constant import *


class TestBurger:

    def test_burger_set_buns(self):
        burger = Burger()
        bun = Bun('Булочка с кунжутом', 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_burger_add_ingredient(self):
        burger = Burger()
        cutlet = Ingredient(INGREDIENT_TYPE_FILLING, 'Мясная котлета грилль', 100)
        burger.add_ingredient(cutlet)
        assert burger.ingredients == [cutlet]

    def test_burger_remove_ingredient(self):
        burger = Burger()
        cutlet = Ingredient(INGREDIENT_TYPE_FILLING, 'Мясная котлета грилль', 100)
        burger.add_ingredient(cutlet)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_burger_move_ingredient(self):
        burger = Burger()
        cutlet = Ingredient(INGREDIENT_TYPE_FILLING, 'Мясная котлета грилль', 100)
        special_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, 'Специальный соус сыр', 100)
        burger.add_ingredient(cutlet)
        burger.add_ingredient(special_sauce)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [special_sauce, cutlet]

    def test_burger_get_price(self):
        bun = Bun('Булочка с кунжутом', 100)
        cutlet = Ingredient(INGREDIENT_TYPE_FILLING, 'Мясная котлета грилль', 100)
        burger = Burger()
        burger.add_ingredient(cutlet)
        burger.set_buns(bun)
        assert burger.get_price() == 300

    def test_burger_get_receipt(self):
        bun = Bun('Булочка с кунжутом', 100)
        cutlet = Ingredient(INGREDIENT_TYPE_FILLING, 'Мясная котлета грилль', 100)
        special_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, 'Специальный соус сыр', 100)
        cucumbers = Ingredient(INGREDIENT_TYPE_FILLING, 'Огурцы', 100)
        salad = Ingredient(INGREDIENT_TYPE_FILLING, 'Салат', 100)
        onion = Ingredient(INGREDIENT_TYPE_FILLING, 'Лук', 100)
        burger = Burger()
        burger.add_ingredient(cutlet)
        burger.add_ingredient(cutlet)
        burger.add_ingredient(special_sauce)
        burger.add_ingredient(cucumbers)
        burger.add_ingredient(salad)
        burger.add_ingredient(onion)
        burger.set_buns(bun)
        assert burger.get_receipt() == BIG_MAC
