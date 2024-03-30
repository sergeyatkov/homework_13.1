from utils.product import Product


class Smartphone(Product):
    """
    Класс описывает объект (смартфон).
    """
    performance: str
    model: str
    memory_capacity: str

    def __init__(self, performance: str, model: str,
                 memory_capacity: str, name: str,
                 description: str, price: float,
                 quantity: int, color: str):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
