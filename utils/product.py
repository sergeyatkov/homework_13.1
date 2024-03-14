class Product:
    """
    Класс описывает объет "Товар"
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"{self.name}, {self.price} руб.\n"
                f"Остаток: {self.quantity} шт.")

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        """
        Метод создает товар, который можно добавлять в список товаров.
        :return: возвращает объект
        """
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Некорректное занчение (цена)")
        self.__price = price

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity: int):
        self.__quantity = new_quantity
