from functions import get_categories_list, parse_category
from utils.category import Category
from utils.product import Product


def main():
    json_file: list[dict] = get_categories_list("data", "products.json")
    item = parse_category(json_file)
    # item[0].add_product("Samsung Galaxy C22 Ultra", "512GB", -2, 43)
    # print(item[0].get_products[3].get_info)
    # item[0].add_product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
    #                     210000.99, 34)
    print(str(item[0].products[0]))
    print(item.__len__())
    print(len(item[0]))
    print(item[0])
    print(item[1])
    print(item[0].products[0].__add__(item[0].products[1]))
    print(item[0].products[1].color)


if __name__ == '__main__':
    main()
