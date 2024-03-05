from utils.product import Product
import pytest

@pytest.fixture
def nike_sneakers():
    return Product("Nike Air Max 90 Halloween", "Sneakers", 13668.99, 100)

def test_init(nike_sneakers):
    assert nike_sneakers.name == "Nike Air Max 90 Halloween"
    assert nike_sneakers.description == "Sneakers"
    assert nike_sneakers.price == 13668.99
    assert nike_sneakers.remaining == 100
