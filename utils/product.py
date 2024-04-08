from utils.mixin_repr import MixinRepr
from utils.any_product import AnyProduct


class Product(AnyProduct, MixinRepr):
    """
    Класс описывает объект "Товар"
    """
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        super().__init__(name, description, price, quantity, color)
        self.name = name
        self.description = description
        self.price = price
        if quantity == 0:
            raise ValueError('Нельзя добавить товар с нулевым количеством!')
        else:
            self.quantity = quantity
        self.color = color

    def __str__(self) -> str:
        """
        Магический метод __str__ выводит информацию о
        позиции товара на экран.
        """
        return (f"{self.name}, цвет: {self.color}, {self.price} руб. "
                f"Остаток: {self.quantity} шт.")

    def __add__(self, other) -> float:
        """
        Магический метод __add__ возвращает
        общую стоимость всего оставшегося товара одной позиции.
        """
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise Exception("Ошибка типа.")

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int, color: str) -> object:
        """
        Метод создает товар, который можно добавлять в список товаров.
        :return: Возвращает объект
        """
        return cls(name, description, price, quantity, color)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price) -> None:
        if price <= 0:
            print("Некорректное занчение (цена)")
        self.__price = price

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        self.__quantity = new_quantity
