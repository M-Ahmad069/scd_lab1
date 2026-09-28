# CSE325-2026-L02-M4RB-T4

import unittest

from grade_report import (
    calculate_average,
    letter_grade,
    performance_status,
)


class TestGradeReport(unittest.TestCase):

    def test_average(self):
        self.assertEqual(calculate_average([85, 78, 92]), 85.0)

    def test_letter_grade(self):
        self.assertEqual(letter_grade(91.67), "A")

    def test_performance_status(self):
        self.assertEqual(performance_status(85.0), "Good")

    def test_empty_grades(self):
        self.assertEqual(calculate_average([]), 0)


if __name__ == "__main__":
    unittest.main()

# Measured against the construction baseline.
# CSE325-2026-L02-M4RB
