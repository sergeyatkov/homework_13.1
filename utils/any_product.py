from abc import ABC, abstractmethod


class AnyProduct(ABC):
    """
    Абстрактный класс.
    Формирует структуру будущих классов наследников.
    """
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.color = color

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
