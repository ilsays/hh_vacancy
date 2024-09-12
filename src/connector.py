import json
from abc import ABC, abstractmethod
from dataclasses import asdict
from src.vacancies import Vacancies
from pathlib import Path


class Connector(ABC):

    """Конструктор класса"""

    @abstractmethod
    def get_vacancy(self) -> list[Vacancies]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancies) -> None:
        pass

    @abstractmethod
    def delete_vacancies(self, vacancy: Vacancies) -> None:
        pass

    @staticmethod
    def _parse_vacancy_to_dict(vacancy: Vacancies) -> dict:
        return asdict(vacancy)

    @staticmethod
    def _parse_dict_to_vacancy(raw_data: dict) -> Vacancies:
        return Vacancies(**raw_data)


class ConnectorJson(Connector):

    """Класс коннектор для получения, удалеия, сохранения вакансий"""
    def __init__(self, file_path: Path, encoding='utf-8') -> None:
        self.file_path = file_path
        self.encoding = encoding

    def get_vacancy(self) -> list[Vacancies]:
        if not self.file_path.exists():
            return []

        vacancies = []
        with self.file_path.open(encoding=self.encoding) as f:
            for item in json.load(f):
                vacancy = self._parse_dict_to_vacancy(item)
                vacancies.append(vacancy)
        return vacancies

    def add_vacancy(self, vacancy: Vacancies) -> None:
        vacancies = self.get_vacancy()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            self._save(*vacancies)

    def delete_vacancies(self, vacancy: Vacancies) -> None:
        vacancies = self.get_vacancy()
        if vacancy in vacancies:
            vacancies.remove(vacancy)
            self._save(*vacancies)

    def _save(self, *vacancies: Vacancies) -> None:
        raw_data = [self._parse_vacancy_to_dict(vac) for vac in vacancies]
        with self.file_path.open(mode='w', encoding=self.encoding) as file:
            json.dump(raw_data, file, indent=2, ensure_ascii=False)
