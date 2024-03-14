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

    def __str__(self):
        return f"{self.name} количество продуктов: {self.__len__()}."

    def __len__(self):
        total_quantity = 0
        for meaning in self.products:
            total_quantity += meaning.quantity
        return total_quantity

    @property
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, name: str, description: str, price: float, quantity: int):
        """
        метод принимает на вход объект товара и добавляет его в список.
        """
        for product in self.products:
            if product.name == name:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return
        product = Product.new_product(name, description, price, quantity)
        self.__products.append(product)
