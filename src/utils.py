import json
from datetime import datetime


def load_json(path):
    """
    Функция для открытия и распаковки файла JSON
    :param path: путь к JSON-файлу
    :return: распакованный JSON
    """
    with open(path) as file:
        return json.load(file)


def sort_list_dict_by_key(dict_list: list[dict], dict_key: str) -> list[dict]:
    """
    Функция сортировки списка словарей по определенному ключу
    :param dict_list: список словарей
    :param dict_key: ключ словарей
    :return: сортированный список словарей по ключу
    """
    sorted_lst = sorted(dict_list, key=lambda x: x[dict_key], reverse=True)
    return sorted_lst


def get_date_from_str(date: str):
    """
    Функция получает дату в формате str в виде %Y-%m-%dT%H:%M:%S.%f
    :param date: дата
    :return: возвращает дату %d.%m.%Y
    """
    the_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return f'{the_date:%d.%m.%Y}'


def hide_account_number(account: str) -> str:
    """
    Функция конвертирует полученный номер счета или карты, скрывая часть информации
    :param account: номер банковского счета или карты
    :return: скрытый номер банковского счета или карты
    """
    if not account:
        return ""
    elif "Счет" in account:
        return "Счет **"+account[-4:]
    else:
        account_list = account.split(" ")
        account_list[-1] = account_list[-1][0:4] + " " + account_list[-1][4:6] + "** **** " + account_list[-1][12:]
        return " ".join(account_list)
