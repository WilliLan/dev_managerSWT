import unittest
from bmi_calculator import calculate_bmi, categorize_bmi

class TestBMICalculator(unittest.TestCase):
    def test_underweight(self):
        self.assertEqual(categorize_bmi(18.4), "Underweight")

    def test_normal_weight(self):
        self.assertEqual(categorize_bmi(18.5), "Normal weight")
        self.assertEqual(categorize_bmi(24.9), "Normal weight")

    def test_overweight(self):
        self.assertEqual(categorize_bmi(25.0), "Overweight")
        self.assertEqual(categorize_bmi(29.9), "Overweight")

    def test_obese(self):
        self.assertEqual(categorize_bmi(30.0), "Obese")
        self.assertEqual(categorize_bmi(35.0), "Obese")

    def test_boundary_shift(self):
        self.assertEqual(categorize_bmi(18.5), "Normal weight")
        self.assertEqual(categorize_bmi(18.4), "Underweight")
    
if __name__ == "__main__":
    unittest.main()
