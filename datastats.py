import math
import json


EMPLOYEE_JSON = """
{
    "age": 28,
    "surname": "Mustermann",
    "name": "Maria",
    "salary": "€35000"
}
"""


def stats(data, iage, isalary):
    # iage and isalary are the starting age and salary used to
    # compute the average yearly increase of salary.

    # Compute average yearly increase
    average_age_increase = math.floor(sum([e['age'] for e in data]) / len(data)) - iage
    average_salary_increase = math.floor(sum([int(e['salary'][1:]) for e in data]) / len(data)) - isalary

    yearly_avg_increase = math.floor(average_salary_increase / average_age_increase)

    # Compute max salary
    salaries = [int(e['salary'][1:]) for e in data]
    threshold = '€' + str(max(salaries))

    max_salary = [e for e in data if e['salary'] == threshold]

    # Compute min salary
    salaries = [int(d['salary'][1:]) for d in data]
    min_salary = [e for e in data if e['salary'] == '€{}'.format(str(min(salaries)))]

    return json.dumps({
        'avg_age': math.floor(sum([e['age'] for e in data]) / len(data)),
        'avg_salary': math.floor(sum([int(e['salary'][1:]) for e in data]) / len(data)),
        'avg_yearly_increase': yearly_avg_increase,
        'max_salary': max_salary,
        'min_salary': min_salary,
    })


def main():
    print(stats(json.loads(f"[{EMPLOYEE_JSON}]"), iage=24, isalary=30000))


if __name__ == "__main__":
    main()
