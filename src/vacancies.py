class Vacancies:

    def __init__(self, name_vacancy: str,
                 url_vacancy: str,
                 city_vacancy: str, salary_from: int | None,
                 salary_to: int | None,
                 salary_currency: str | None,
                 description_vacancy: str) -> None:
        self.name_vacancy = name_vacancy
        self.url_vacancy = url_vacancy
        self.city_vacancy = city_vacancy

        if self._validation(salary_from) is None:
            if salary_from is None:
                self.salary_from = 0
            else:
                self.salary_from = salary_from

        if self._validation(salary_to) is None:
            if salary_to is None:
                self.salary_to = 0
            else:
                self.salary_to = salary_to

        self.salary_currency = salary_currency
        self.description_vacancy = description_vacancy

    @staticmethod
    def _validation(salary):
        """
        Метод класса осуществляющий валидацию заработной платы вакансий
        """
        if salary is not None and salary < 0:
            raise ValueError("Salary cannot be negative")

    def __str__(self):
        return (f"""Наименование вакансии: {self.name_vacancy}
Город, в котором расположен офис компании: {self.city_vacancy} 
Заработная плата: от {self.salary_from} - до {self.salary_to} {self.salary_currency}
Описание вакансии: {self.description_vacancy}""")

    def __repr__(self):
        return f"""{self.__class__.__name__}({self.name_vacancy}, {self.url_vacancy}, {self.city_vacancy},
{self.salary_to}, {self.salary_from}, {self.salary_currency}, {self.description_vacancy}"""

    def __le__(self, other):
        if self.salary_to and other.salary_to:
            return self.salary_to <= other.salary_to

        if self.salary_from and other.salary_from:
            return self.salary_from <= other.salary_from
