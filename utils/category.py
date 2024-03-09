from utils.product import Product


class Category:
    """
    Класс описывает объект "Категория товара"
    """
    name: str
    description: str
    __products: list[Product]

    total_number_cat = 0
    total_number_unic_prod = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_number_cat += 1
        Category.total_number_unic_prod += len(products)

    @property
    def get_products(self) -> list[Product]:
        return self.__products

    def add_product(self, product: [Product]):
        """
        метод принимает на вход объект товара и добавляет его в список.
        """
        self.__products.append(product)

