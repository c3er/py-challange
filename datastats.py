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


def stats(employees_data, starting_age, starting_salary):
    # starting_age and starting_salary are used to compute the average yearly increase of salary.

    # Compute average yearly increase
    average_age_increase = math.floor(sum([employee['age'] for employee in employees_data]) / len(employees_data)) - starting_age
    average_salary_increase = math.floor(sum([int(employee['salary'][1:]) for employee in employees_data]) / len(employees_data)) - starting_salary
    yearly_avg_increase = math.floor(average_salary_increase / average_age_increase)

    # Compute max salary
    salaries = [int(employee['salary'][1:]) for employee in employees_data]
    threshold = '€' + str(max(salaries))
    max_salary = [employee for employee in employees_data if employee['salary'] == threshold]

    # Compute min salary
    salaries = [int(employee['salary'][1:]) for employee in employees_data]
    min_salary = [employee for employee in employees_data if employee['salary'] == '€{}'.format(str(min(salaries)))]

    return json.dumps({
        'avg_age': math.floor(sum([employee['age'] for employee in employees_data]) / len(employees_data)),
        'avg_salary': math.floor(sum([int(e['salary'][1:]) for e in employees_data]) / len(employees_data)),
        'avg_yearly_increase': yearly_avg_increase,
        'max_salary': max_salary,
        'min_salary': min_salary,
    })


def main():
    print(stats(json.loads(f"[{EMPLOYEE_JSON}]"), starting_age=24, starting_salary=30000))


if __name__ == "__main__":
    main()
