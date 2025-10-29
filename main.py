from src.file_readers import csv_reader
from src.file_readers import excel_reader
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.utils import read_json
from src.validations import process_bank_search
from src.widget import get_date
from src.widget import mask_account_card


def main() -> None:
    """
    Функция отвечает за основную логику проекта и связывает функциональности между собой
    :return: None
    """
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
    )

    while True:
        file_type = input("Выберите необходимый пункт меню: ").strip()
        if file_type == "1":
            print("Для обработки выбран JSON-файл\n")
            transactions_list = read_json("operations")
            break
        elif file_type == "2":
            print("Для обработки выбран CSV-файл \n")
            transactions_list = csv_reader("transactions")
            break
        elif file_type == "3":
            print("Для обработки выбран XLSX-файл \n")
            transactions_list = excel_reader("transactions_excel")
            break
        else:
            print(" Выберите корректный пункт меню \n")
    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
            """
        )
        status = input("Введите статус: ").strip().upper()
        if status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Статус операции "{status}" недоступен \n')
        else:
            filtered_transactions = filter_by_state(transactions_list, status)
            print(f'Операции отфильтрованы по статусу "{status}" \n')
            break
    while True:
        print("Отсортировать операции по дате? Да/Нет\n")
        sort = input("Введите  Да или Нет: ").strip().lower()

        if sort == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?\n")
                rev = input("Введите возрастаниe или убывание:").strip().lower()
                if rev == "возрастаниe":
                    filtered_transactions = sort_by_date(filtered_transactions, False)
                    break
                elif rev == "убывание":
                    filtered_transactions = sort_by_date(filtered_transactions)
                    break
                else:
                    print("Выберите корректную сортировку \n")
            break
        elif sort == "нет":
            break
        else:
            print("Введите  корректные данные \n")
    while True:
        print("Выводить только рублевые транзакции? Да/Нет \n")
        sort_currency = input("Введите  Да или Нет: ").strip().lower()
        if sort_currency == "да":
            filtered_transactions = process_bank_search(filtered_transactions, "RUB")
            break
        elif sort_currency == "нет":
            break
        else:
            print("Введите  корректные данные\n")
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        filtering_with_word = input("Введите  Да или Нет: ").strip().lower()
        if filtering_with_word == "да":
            search_word = input("Введите определенноe словo: ").strip()
            filtered_transactions = process_bank_search(filtered_transactions, search_word)
            break
        elif filtering_with_word == "нет":
            break
        else:
            print("Введите  корректные данные\n")
    print("\n\nРаспечатываю итоговый список транзакций... \n")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
    if filtered_transactions:
        for transaction in filtered_transactions:
            date = get_date(transaction.get("date"))
            description = transaction.get("description")
            from_card = mask_account_card(transaction.get("from", ""))
            to_card = mask_account_card(transaction.get("from"))
            amount = transaction.get("operationAmount").get("amount")
            currency = transaction.get("operationAmount").get("currency").get("code")
            if from_card:
                print(f"{date} {description}\n{from_card} -> {to_card}\nСумма: {amount} {currency}\n")
            else:
                print(f"{date} {description}\n{to_card}\nСумма: {amount} {currency}\n")
    else:
        print(" Не найдено ни одной транзакции, подходящей под вашиусловия фильтрации")


if __name__ == "__main__":
    main()
