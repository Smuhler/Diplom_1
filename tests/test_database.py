from praktikum.database import *
from tests.helpers import *


class TestDatabase:

    def test_database_available_buns(self):
        database = Database()
        database.buns = buns
        assert database.available_buns() == buns

    def test_database_available_ingredients(self):
        database = Database()
        database.ingredients = ingredients
        assert database.available_ingredients() == ingredients
