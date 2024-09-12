from abc import ABC, abstractmethod
from typing import List

import requests
import json
import time
from src.vacancies import Vacancies


class Base(ABC):

    """Конструктор класса для работы с API"""

    @abstractmethod
    def get_vacancies(self, search: str) -> list[dict]:
        pass


class HHVacancies(Base):

    """Класс для работы с API HeadHunter"""

    def get_vacancies(self, search: str) -> list[Vacancies]:

        """ Метод класса, который запрашивает информацию по вакаснсиям на сайте hh.ru"""

        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': search,
            'only_with_salary': True,
            'per_page': 100,
        }

        raw_vacancies = self._get_list(url, params, max_pages=2)
        return [
            Vacancies(
                name=data['name'],
                url=data['alternate_url'],
                salary_currency=data['salary']['currency'],
                salary_from=data['salary']['from'],
                salary_to=data['salary']['to'],
            )
            for data in raw_vacancies
        ]

    def _get_list(self, url: str, params: dict, max_pages: int = 1) -> list[dict]:

        items = []
        for current_page in range(1, max_pages):
            params['page'] = current_page
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data['found'] == 0:
                break

            items.extend(data['items'])

        return items
