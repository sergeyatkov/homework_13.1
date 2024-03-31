from utils.product import Product


class LawnGrass(Product):
    """
    Класс описывает объект (газонная трава).
    """
    manufacturer_country: str
    germination_period: str

    def __init__(self, manufacturer_country: str, germination_period: str,
                 name: str, description: str, price: float,
                 quantity: int, color: str):
        super().__init__(name, description, price, quantity, color)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
