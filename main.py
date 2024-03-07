from functions import get_categories_list, parse_category


def main():
    json_file: list[dict] = get_categories_list("data", "products.json")
    parse_category(json_file)


if __name__ == '__main__':
    main()
