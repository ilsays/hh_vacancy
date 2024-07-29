import requests
import json


class Currency:
    """
    Класс записи полученной информации при парсинге
    """

    def __init__(self, file_currency) -> None:
        self.file_currency = file_currency

    def save_currency(self, currency) -> None:
        """
        Метод, записывающий и сохраняющий полученную информации
        """

        with open(self.file_currency, "w", encoding="utf-8") as file:
            json.dump(currency, file, indent=4)


class ParserCurrency(Currency):
    """
    Класс парсер актуальной информации по курсу валют
    """

    def __init__(self, file_currency) -> None:
        self.__url = "https://www.cbr-xml-daily.ru/daily_json.js"
        self.currency = []
        super().__init__(file_currency)

    def load_currency(self) -> None:
        """
        Метод, получающий актуальные на сегодняшний день курс валют
        """
        response = requests.get(self.__url)
        currency = response.json()
        self.currency.append(currency)
        super().save_currency(self.currency)
