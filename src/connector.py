import copy
import json
from abc import ABC, abstractmethod
from src.vacancies import Vacancies
import os
from src.currency_hh_api import ParserCurrency


class BaseConnector(ABC):

    @abstractmethod
    def create_vacancy_list(self) -> list:
        pass

    @abstractmethod
    def add_vacancy(self) -> None:
        pass

    @abstractmethod
    def get_info(self, key_name: str, value_name: str | int) -> list:
        pass

    @abstractmethod
    def delete_vacancy(self) -> None:
        pass

    @staticmethod
    def filter_vacancy(dict_vacancy: dict, key_name: str, value_name: int | str):
        pass


class Connector(BaseConnector):

    def __init__(self, name_file: str) -> None:
        self._vacancy_list = []
        self._finish_list = []
        self.name_file = name_file

    @staticmethod
    def filter_vacancy(dict_vacancy: dict, key_name: str, value_name: int | str):

        if value_name == dict_vacancy[key_name]:
            return True
        else:
            return False

    def create_vacancy_list(self) -> list:
        """
        Метод класса для формирования списка вакансий по новому
        """

        with open(self.name_file, "r", encoding="utf-8") as file:
            read_vacancy_file = json.load(file)
            for item in read_vacancy_file:
                if item["salary"] is None or item["area"] is None:
                    continue
                else:
                    self._vacancy_list.append(Vacancies(item["name"], item["alternate_url"], item["area"]["name"],
                                                        item["salary"]["from"], item["salary"]["to"],
                                                        item["salary"]["currency"], item["snippet"]["requirement"]))
        return self._vacancy_list

    def add_vacancy(self) -> None:
        vacancy_list = self.create_vacancy_list()
        new_vac = []
        file_currency = "../hh_vacancies/data/currency_today.json"
        currency_today = ParserCurrency(file_currency)
        currency_today.load_currency()

        with open(self.name_file, "w", encoding="utf-8") as file:
            for f in vacancy_list:
                if f.salary_currency != "RUR" and f.salary_currency != "" and f.salary_currency != "BYR":
                    file_ = open(file_currency, "r", encoding="utf-8")
                    load_file = json.load(file_)
                    salary_from = round(f.salary_from * load_file[0]["Valute"][f"{f.salary_currency}"]["Value"] /
                                        load_file[0]["Valute"][f"{f.salary_currency}"]["Nominal"])
                    salary_to = round(f.salary_from * load_file[0]["Valute"][f"{f.salary_currency}"]["Value"] /
                                      load_file[0]["Valute"][f"{f.salary_currency}"]["Nominal"])
                    currency = f"RUR, сконвертировано из {f.salary_currency}"
                    file_.close()
                else:
                    salary_from = f.salary_from
                    salary_to = f.salary_to
                    currency = f.salary_currency

                new_vac.append({"name": f.name_vacancy, "url": f.url_vacancy, "area": f.city_vacancy,
                                "salary_from": salary_from, "salary_to": salary_to,
                                "currency": currency, "snippet": f.description_vacancy})

            return json.dump(new_vac, file, indent=4)

    def get_info(self, key_name: str, value_name: str | int) -> list:
        """
        Метод класс возвращающий информацию по вакансиям по ключевым словам полученным о пользователя
        """
        with open(self.name_file, "r", encoding="utf-8") as file:
            top_list = json.load(file)
            for item in top_list:
                if self.filter_vacancy(item, key_name, value_name) is True:
                    self._finish_list.append(item)
                else:
                    continue
            return self._finish_list

    def __str__(self, *args):
        return f"{self.get_info(*args)}"

    def delete_vacancy(self) -> None:
        """
        Метод удаляющий файл *.json содержащий вакансии сформированный в соответсвии с заданной структурой
        """

        os.remove(self.name_file)
