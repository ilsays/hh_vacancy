from dataclasses import dataclass


@dataclass
class Vacancies:

    name: str
    url: str
    salary_currency: str = 'RUR'
    salary_from: int | None = None
    salary_to: int | None = None

    def __post_init__(self):

        self._validation(self.salary_from)
        self._validation(self.salary_to)

    @staticmethod
    def _validation(salary: int | None) -> None:
        """
        Метод класса осуществляющий валидацию заработной платы вакансий
        """

        if salary is not None:
            assert salary > 0

    def __lt__(self, other: 'Vacancies') -> bool:

        if self.salary_from and other.salary_from:
            return self.salary_from < other.salary_from

        if self.salary_to and other.salary_to:
            return self.salary_to < other.salary_to

        self_salary = self.salary_from or self.salary_to
        other_salary = other.salary_from or other.salary_to
        return self_salary < other_salary

    def __eq__(self, other: 'Vacancies') -> bool:

        eq_from = self.salary_from == other.salary_from
        eq_to = self.salary_to == other.salary_to

        return eq_from and eq_to


