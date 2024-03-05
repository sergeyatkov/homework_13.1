from utils.category import Category
import pytest


@pytest.fixture
def boots():
    return Category("Boots", "Shoes", ["Sneakers", "Boots", "Slippers"])


def test_init(boots):
    assert boots.name == "Boots"
    assert boots.description == "Shoes"
    assert boots.goods == ["Sneakers", "Boots", "Slippers"]
