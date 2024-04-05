from utils.any_category import AnyCategory
from utils.product import Product


class Category(AnyCategory):
    """
    Класс описывает объект "Категория товара"
    """
    name: str
    description: str
    __products: list[Product]

    total_number_cat = 0
    total_number_unic_prod = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        super().__init__(name, description, products)
        self.name = name
        self.description = description
        self.__products = products

        Category.total_number_cat += 1
        Category.total_number_unic_prod += len(products)

    def __str__(self) -> str:
        """
        Магический метод __str__ возвращает
        название категории и количество продуктов в ней.
        """
        return f"{self.name} количество продуктов: {self.__len__()}."

    def __len__(self) -> int:
        """
        Магический метод __len__ возвращает
        общее количество товаров в данной категории
        """
        total_quantity = 0
        for meaning in self.products:
            total_quantity += meaning.quantity
        return total_quantity

    @property
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, item) -> None:
        """
        Метод принимает на вход объект товара, проверяет задвоение позиций товара,
        корректирует количество на остатках и цену товара,
        затем добавляет его в список.
        """
        if not isinstance(item, Product):
            raise Exception("Некорректный объект.")
        for product in self.products:
            if product.name == item.name:
                product.quantity += item.quantity
                if product.price < item.price:
                    product.price = item.price
                return
        product = Product.new_product(item.name, item.description, item.price, item.quantity, item.color)
        self.__products.append(product)
