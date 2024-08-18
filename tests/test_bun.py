import pytest
from praktikum.bun import *


class TestBun:

    @pytest.mark.parametrize('name', ['', 'Lorem ipsum dolor sit amet, consectetuer '])
    def test_bun_get_name(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [-100, -0.1, 0, 0.1, 100])
    def test_bun_get_price(self, price):
        bun = Bun('Булочка с кунжутом', price)
        assert bun.price == price

