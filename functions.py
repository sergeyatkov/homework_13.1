from pathlib import Path
import json
from utils.category import Category
from utils.product import Product


def get_categories_list(path, file_name) -> list[dict]:
    """
        Функция берет данные из файла json
        :param path: путь к файлу.
        :param file_name: имя файла.
        :return: возвращает данные из файла.
        """
    path = Path(__file__).parent.joinpath(path, file_name)
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def parse_products(products: dict[Product]) -> list:
    """
    Функция создает экземпляры класса Product
    и помещает данные в список.
    :param products: словарь с инф. о товаре.
    :return: список с инф. о товаре.
    """
    list_product = []
    for product in products:
        pa = Product(
            name=product["name"],
            description=product["description"],
            price=product["price"],
            quantity=product["quantity"]
        )
        list_product.append(pa)
    return list_product


def parse_category(json_file) -> list:
    """
    Функция создает экземпляры класса Category.
    и помещает данные в список.
    :param json_file: .json файл
    :return: список с категориями
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
