class Vacancies:

    def __init__(self, url_vacancy: str,
                 name_vacancy: str,
                 city_vacancy: str,
                 description_vacancy: str,
                 salary_from: int | None,
                 salary_to: int | None,
                 salary_currency: str | None,
                 ) -> None:
        self.url_vacancy = url_vacancy
        self.name_vacancy = name_vacancy
        self.city_vacancy = city_vacancy
        self.description_vacancy = description_vacancy
        self.salary_currency = salary_currency

        if self.validation(salary_from) is None:
            if salary_from is None:
                self.salary_from = 0
            else:
                self.salary_from = salary_from

        if self.validation(salary_to) is None:
            if salary_to is None:
                self.salary_to = 0
            else:
                self.salary_to = salary_to

    def __str__(self):
        return f'''Вакансия: {self.name_vacancy}
Ссылка на вакансию: {self.url_vacancy}
Зарплата: от {self.salary_from} до {self.salary_to} {self.salary_currency}
Описание вакансии: {self.description_vacancy}
Город: {self.city_vacancy}'''

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name_vacancy}, {self.url_vacancy}, {self.city_vacancy}, "
                f"{self.salary_to}, {self.salary_from}, {self.salary_currency}, {self.description_vacancy})")

    @staticmethod
    def validation(salary):

        if salary is not None and salary < 0:
            raise ValueError('Зарплата не может быть отрицательная')

    def __le__(self, other):
        if self.salary_to and other.salary_to:
            return self.salary_to <= other.salary_to

        if self.salary_from and other.salary_from:
            return self.salary_from <= other.salary_from
