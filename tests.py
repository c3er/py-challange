import json
import unittest

import datastats


EMPLOYEES_JSON = """
[
    {
        "age": 28,
        "surname": "Mustermann",
        "name": "Maria",
        "salary": "€35000"
    }
]
"""


class DataStatsTests(unittest.TestCase):
    def test_basic_case(self):
        EMPLOYEES_JSON = """
        [
            {
                "age": 28,
                "surname": "Mustermann",
                "name": "Maria",
                "salary": "€35000"
            }
        ]
        """
        expected = {
            "avg_age": 28,
            "avg_salary": 35000,
            "avg_yearly_increase": 1250,
            "max_salary": [
                {
                    "age": 28,
                    "surname": "Mustermann",
                    "name": "Maria",
                    "salary": "€35000",
                },
            ],
            "min_salary": [
                {
                    "age": 28,
                    "surname": "Mustermann",
                    "name": "Maria",
                    "salary": "€35000",
                },
            ],
        }
        self.assertEqual(
            json.loads(datastats.stats(EMPLOYEES_JSON, starting_age=24, starting_salary=30000)),
            expected)

    def test_multiple_employees(self):
        EMPLOYEES_JSON = """
        [
            {
                "age": 28,
                "surname": "Mustermann",
                "name": "Maria",
                "salary": "€35000"
            },
            {
                "age": 40,
                "surname": "Müller",
                "name": "Karl",
                "salary": "€70000"
            },
            {
                "age": 35,
                "surname": "Schmidt",
                "name": "Klaus",
                "salary": "€40000"
            }
        ]
        """
        expected = {
            "avg_age": 34,
            "avg_salary": 48333.33,
            "avg_yearly_increase": 1774.19,
            "max_salary": [
                {
                    "age": 40,
                    "surname": "Müller",
                    "name": "Karl",
                    "salary": "€70000"
                }
            ],
            "min_salary": [
                {
                    "age": 28,
                    "surname": "Mustermann",
                    "name": "Maria",
                    "salary": "€35000"
                }
            ]
        }
        self.assertEqual(
            json.loads(datastats.stats(EMPLOYEES_JSON, starting_age=24, starting_salary=30000)),
            expected)


if __name__ == "__main__":
    unittest.main()
