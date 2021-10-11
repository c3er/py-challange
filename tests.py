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
                    "salary": "\u20ac35000",
                },
            ],
            "min_salary": [
                {
                    "age": 28,
                    "surname": "Mustermann",
                    "name": "Maria",
                    "salary": "\u20ac35000",
                },
            ],
        }
        self.assertEqual(
            json.loads(datastats.DataStats().stats(json.loads(EMPLOYEES_JSON), iage=24, isalary=30000)),
            expected)


if __name__ == "__main__":
    unittest.main()
