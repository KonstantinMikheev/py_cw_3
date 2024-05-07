import json


def load_json(path: str):
    """
    Функция для открытия и распаковки файла JSON
    :param path: путь к JSON-файлу
    :return: распакованный JSON
    """
    with open(path) as file:
        return json.load(file)
