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

    @property
    def get_info(self):
        return (f"{self.name}, {self.price} руб. "
                f"Остаток: {self.quantity} шт.")

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        """
        Метод создает товар, который можно добавлять в список товаров.
        :return: возвращает объект
        """
        cls.name = name
        cls.description = description
        cls.price = price
        cls.quantity = quantity
        return cls(name, description, price, quantity)

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
        if price <= 0:
            print("Некорректное занчение (цена)")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity: int):
        self.quantity = new_quantity
