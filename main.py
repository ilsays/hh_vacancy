from src.hh_api import HHVacancies
from src.configuration import DATA_DIR
from src.connector import ConnectorJson
from src.user_usage import start_user_interaction

VACANCIES_PATH = DATA_DIR / "vacancies.json"

api_client = HHVacancies()
connector = ConnectorJson(VACANCIES_PATH)


def main():

    """Основная работа программы"""

    search_text = input('Введите текст для поиска вакансий: ')

    print('Получаем вакансии...')
    vacancies = api_client.get_vacancies(search_text)

    print('Сохраняем в базу')
    for vac in vacancies:
        connector.add_vacancy(vac)

    start_user_interaction(connector)


if __name__ == "__main__":
    main()



