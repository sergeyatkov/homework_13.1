class Category:
    """
    Класс описывает объект "Категория товара"
    """
    name: str
    description: str
    goods: list

    total_number_cat = 0
    total_number_unic_cat = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.goods = goods

        Category.total_number_cat += 1
