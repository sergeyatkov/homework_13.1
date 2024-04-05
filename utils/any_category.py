from abc import ABC, abstractmethod
from utils.product import Product


class AnyCategory(ABC):
    """
    Абстрактный класс.
    Формирует структуру будущих классов наследников.
    """
    name: str
    description: str
    __products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass
