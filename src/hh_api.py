from abc import ABC, abstractmethod
import requests
import json


class Base(ABC):

    @abstractmethod
    def __init(self):
        pass


class Parser(ABC):

    def __init__(self, api_work) -> None:
        self.api_work = api_work

    def file_saving(self, vacancies) -> None:
        with open(self.api_work, "w", encoding='utf-8') as file:
            json.dump(vacancies, file)


class VacanciesHH(Parser):

    def __init__(self, api_work) -> None:
        self.vacancies = []
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.parameters = {'text': '', 'page': 0, 'per_page': 100}
        super().__init__(api_work)

    def load_vacancies(self, user_input) -> None:
        """
        Метод класса VacanciesHH(Parser), который запрашивает информацию по вакаснсиям на сайте hh.ru
        :param user_input: наименовании запрашиваемой вакансии
        """
        self.parameters['text'] = user_input
        while self.parameters.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.parameters, timeout=10)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.parameters['page'] += 1
        super().file_saving(self.vacancies)
