from abc import ABC, abstractmethod
import requests
import json


class Base(ABC):
    """
    Конструктор класса для работы с API
    """

    @abstractmethod
    def __init__(self):
        pass


class Parser(ABC):

    def __init__(self, api_work) -> None:
        self.api_work = api_work

    def file_saving(self, vacancies) -> None:
        """
        Метод класса Parser(BaseHH) записывающий в файл *.json всю информацию по вакансиям
        """

        with open(self.api_work, "w", encoding='utf-8') as file:
            json.dump(vacancies, file, indent=4)


class VacanciesHH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, api_work) -> None:
        self.vacancies = []
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.parameters = {'text': '', 'page': 0, 'per_page': 100}
        super().__init__(api_work)

    def load_vacancies(self, user_input) -> None:
        """
        Метод класса VacanciesHH(Parser),
        который запрашивает информацию по вакаснсиям на сайте hh.ru
        """

        self.parameters['text'] = user_input
        while self.parameters.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.parameters, timeout=10)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.parameters['page'] += 1
        super().file_saving(self.vacancies)
