from src.connector import Connector
from prettytable import PrettyTable


def start_user_interaction(connector: Connector):
    while True:
        print(
            'Действия:\n',
            '1. Получить топ вакансий\n',
            '0. Выйти'
        )
        user_command = input()

        if user_command == '1':
            print_top_vacancies(connector)
        elif user_command == '0':
            return


def print_top_vacancies(connector: Connector):
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancies = connector.get_vacancy()

    t = PrettyTable(['Название', 'Ссылка', 'Зарплата, от', 'Зарплата, до', 'Валюта'])
    for vac in sorted(vacancies)[:top_n]:
        t.add_row([vac.name, vac.url, vac.salary_from or '- ', vac.salary_to or '- ', vac.salary_currency or '- '])
    print(t)