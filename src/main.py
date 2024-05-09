from src.settings import OPERATIONS
from src.utils import get_date_from_str, hide_account_number, load_json, sort_list_dict_by_key


def main():
    executed_list = []
    operation_list = load_json(OPERATIONS)  # Загружаем данные из json-файла
    for the_operation in operation_list:
        # !!!Вопрос!!! Почему при использовании the_operation['state'] выводит ошибку, что ключ не найден?
        # При методе get() все получается. Отдельно выводил ради интереса через operation_list[0]['state'], проблем нет.
        if the_operation.get('state') == "EXECUTED":
            executed_list.append(the_operation)  # Отфильтровываем в новый список успешные транзакции
    # Сортируем от последних к ранним транзакции
    sorted_operation_list = sort_list_dict_by_key(executed_list, "date")
    sorted_last_operation_list = sorted_operation_list[:5]  # Оставляем последние 5 операций
    # Проверка наличия атрибутов с ключами from, to, description. Вывод сформированного отчета по каждой операции
    for dictionary in sorted_last_operation_list:
        if not dictionary.get("description"):
            dictionary["description"] = ""
        if not dictionary.get("from"):
            dictionary["from"] = ""
        if not dictionary.get("to"):
            dictionary["to"] = ""
        converted_date = get_date_from_str(dictionary.get('date'))  # Получение даты в нужном формате
        # Получение счета отправления в требуемом формате
        hidden_account_from = hide_account_number(dictionary.get('from'))
        # Получение счета получателя в требуемом формате
        hidden_account_to = hide_account_number(dictionary.get('to'))
        # !!!Вопрос!!! Эта проблема отняла у меня 1,5 дня, а ответа на вопрос так и нет. Почему при выводе через return
        # в цикле выводится только 1й случай из цикла, а при использовании print все 5? В чем ошибка?
        print(f"""{converted_date} {dictionary.get('description')}
            \r{hidden_account_from} -> {hidden_account_to}"
            \r{dictionary['operationAmount']['amount']} {dictionary['operationAmount']['currency']['name']}\n""")


if __name__ == '__main__':
    main()
