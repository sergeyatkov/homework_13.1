class Product:
    """
    Класс описывает объет "Товар"
    """
    name: str
    description: str
    price: float
    remaining: int

    def __init__(self, name: str, description: str, price: float, remaining: int):
        self.name = name
        self.description = description
        self.price = price
        self.remaining = remaining
