from src.vacancies import Vacancies


def test_one__le__():
    work_vacancy_one = Vacancies("test", "https://url", "Racoon", 100,
                                 330, "USD", "Work to Racoon-city ")
    work_vacancy_two = Vacancies("test", "https://url", "Racoon", 1000,
                                 3200, "USD", "Work to Racoon-city ")
    work_vacancy_three = Vacancies("test", "https://url", "Racoon", 10010,
                                   12230, "USD", "Work to Racoon-city ")
    work_vacancy_four = Vacancies("test", "https://url", "Racoon", 10010,
                                  12230, "USD", "Work to Racoon-city ")
    assert work_vacancy_one.salary_from < work_vacancy_two.salary_from
    assert work_vacancy_three.salary_from == work_vacancy_four.salary_from
    assert work_vacancy_one.salary_to < work_vacancy_two.salary_to
    assert work_vacancy_three.salary_to == work_vacancy_four.salary_to
    assert work_vacancy_four.salary_to > work_vacancy_one.salary_to
    assert work_vacancy_three.salary_from > work_vacancy_two.salary_from
