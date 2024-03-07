from utils.category import Category
import pytest

from utils.product import Product


@pytest.fixture
def cat_1():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации,"
                    " но и получение дополнительных функций для удобства жизни",
                    [Product("Samsung Galaxy C23 Ultra",
                             "256GB, Серый цвет, 200MP камера", 180000.0, 5)])


def test_init(cat_1):
    assert cat_1.name == "Смартфоны"
    assert cat_1.description == ("Смартфоны, как средство не только коммуникации,"
                                 " но и получение дополнительных функций для удобства жизни")
    assert cat_1.products[0].price == 180000.0
    assert cat_1.products[0].name == "Samsung Galaxy C23 Ultra"
    assert cat_1.products[0].description == "256GB, Серый цвет, 200MP камера"
    assert cat_1.products[0].quantity == 5
    assert cat_1.total_number_cat == 1
    assert cat_1.total_number_unic_prod == 1
