from utils.category import Category
import pytest


@pytest.fixture
def cat_1():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации,"
                    " но и получение дополнительных функций для удобства жизни",
                    [])


def test_init(cat_1):
    assert cat_1.name == "Смартфоны"
    assert cat_1.description == ("Смартфоны, как средство не только коммуникации,"
                                 " но и получение дополнительных функций для удобства жизни")
    assert cat_1.goods == []
