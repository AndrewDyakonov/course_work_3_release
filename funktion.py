import json


def get_json_to_list():
    """
    Получить список операций из файла operation.json
    :return:
    """
    with open('operations.json', 'r', encoding="UTF-8") as file:
        list_operation = json.load(file)
    return list_operation


