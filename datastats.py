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


class Employee:
    def __init__(self, surname, name, age, salary, currency):
        self.surname = surname
        self.name = name
        self.age = age
        self.salary = salary
        self.currency = currency

    @classmethod
    def from_json(cls, data):
        if isinstance(data, str):
            data = json.loads(data)

        if isinstance(data, dict):
            return cls(
                data["surname"],
                data["name"],
                data["age"],
                int(data["salary"][1:]),
                data["salary"][0])
        elif isinstance(data, list):
            return [cls.from_json(employee_data) for employee_data in data]
        else:
            raise ValueError("Given JSON could not be parsed")

    def to_dict(self):
        return {
            "age": self.age,
            "surname": self.surname,
            "name": self.name,
            "salary": f"{self.currency}{self.salary}",
        }


def stats(employees_data, starting_age, starting_salary):
    # starting_age and starting_salary are used to compute the average yearly increase of salary.

    employees = Employee.from_json(employees_data)

    average_age_increase = math.floor(sum([employee.age for employee in employees]) / len(employees)) - starting_age
    average_salary_increase = math.floor(sum([employee.salary for employee in employees]) / len(employees)) - starting_salary
    yearly_avg_increase = math.floor(average_salary_increase / average_age_increase)

    salaries = [employee.salary for employee in employees]
    max_salary_employees = [employee for employee in employees if employee.salary == max(salaries)]
    min_salary_employees = [employee for employee in employees if employee.salary == min(salaries)]

    return json.dumps({
        'avg_age': math.floor(sum([employee.age for employee in employees]) / len(employees)),
        'avg_salary': math.floor(sum([employee.salary for employee in employees]) / len(employees)),
        'avg_yearly_increase': yearly_avg_increase,
        'max_salary': [employee.to_dict() for employee in max_salary_employees],
        'min_salary': [employee.to_dict() for employee in min_salary_employees],
    })


def main():
    print(stats(f"[{EMPLOYEE_JSON}]", starting_age=24, starting_salary=30000))


if __name__ == "__main__":
    main()
