from pathlib import Path
import json
from utils.category import Category
from utils.product import Product


def get_categories_list(path, file_name) -> list[dict]:
    """
        Функция берет данные из файла json
        :param path: Путь к файлу.
        :param file_name: Имя файла.
        :return: Возвращает данные из файла.
        """
    path = Path(__file__).parent.joinpath(path, file_name)
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def parse_products(products: dict[Product]) -> list[Product]:
    """
    Функция создает экземпляры класса Product
    и помещает данные в список.
    :param products: Словарь с инф. о товаре.
    :return: Список с инф. о товаре.
    """
    list_product = []
    for product in products:
        item = Product(
            name=product["name"],
            description=product["description"],
            price=product["price"],
            quantity=product["quantity"],
            color=product["color"]
        )
        list_product.append(item)
    return list_product


def parse_category(json_file) -> list[Category]:
    """
    Функция создает экземпляры класса Category
    и помещает данные в список.
    :param json_file: .json файл
    :return: Список с категориями
    """
    categories_list = []
    for category in json_file:
        item = Category(
            name=category["name"],
            description=category["description"],
            products=parse_products(category["products"])
        )
        categories_list.append(item)
    return categories_list
