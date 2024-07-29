from src.hh_api import VacanciesHH
from src.user_usage import interface
from src.connector import Connector


def main():
    user_input = input("Введите название вакансии: ")
    user_request = VacanciesHH(f"../hh_vacancies/data/{user_input}_vacancies.json")

    print("Ожидаем получения данных по вакансиям...")

    user_request.load_vacancies(user_input)

    print("Данные записаны")

    connect = Connector(f"../hh_vacancies/data/{user_input}_vacancies.json")
    connect.add_vacancy()
    interface(f"../hh_vacancies/data/{user_input}_vacancies.json")


if __name__ == "__main__":
    main()
