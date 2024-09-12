import pytest
from src.vacancies import Vacancies


def test_vacancy_compare_by_salary_from():
    v1 = Vacancies('name', 'url', salary_from=10)
    v2 = Vacancies('name', 'url', salary_from=20)
    v3 = Vacancies('name', 'url', salary_from=20)
    assert v1 < v2
    assert v2 == v3
    assert v3 > v1


def test_vacancy_compare_by_salary_to():
    v1 = Vacancies('name', 'url', salary_to=10)
    v2 = Vacancies('name', 'url', salary_to=20)
    v3 = Vacancies('name', 'url', salary_to=20)
    assert v1 < v2
    assert v2 == v3
    assert v3 > v1


def test_vacancy_compare_by_different_salary():
    v1 = Vacancies('name', 'url', salary_to=10)
    v2 = Vacancies('name', 'url', salary_from=20)
    assert v1 < v2


def test_test_equal_vacancies():
    v2 = Vacancies('name_1', 'url', salary_to=20)
    v3 = Vacancies('name_2', 'url', salary_to=20)
    assert v2 == v3
