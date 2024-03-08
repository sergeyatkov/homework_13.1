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
        cls.name, cls.description, cls.price, cls.quantity = input().split()
        return cls(name, description, price, quantity)
