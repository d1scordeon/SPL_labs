from lab2 import Calculator
import unittest


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_positive(self):
        self.calc.x = 5
        self.calc.y = 3
        self.calc.operator = '+'
        self.assertEqual(self.calc.calculation(), 8)

    def test_add_negative(self):
        self.calc.x = -5
        self.calc.y = -3
        self.calc.operator = '+'
        self.assertEqual(self.calc.calculation(), -8)

    def test_sub_positive(self):
        self.calc.x = 5
        self.calc.y = 3
        self.calc.operator = '-'
        self.assertEqual(self.calc.calculation(), 2)

    def test_sub_negative(self):
        self.calc.x = -5
        self.calc.y = -3
        self.calc.operator = '-'
        self.assertEqual(self.calc.calculation(), -2)

    def test_mult_positive(self):
        self.calc.x = 5
        self.calc.y = 3
        self.calc.operator = '*'
        self.assertEqual(self.calc.calculation(), 15)

    def test_mult_negative(self):
        self.calc.x = -5
        self.calc.y = -3
        self.calc.operator = '*'
        self.assertEqual(self.calc.calculation(), 15)

    def test_mult_zero(self):
        self.calc.x = 5
        self.calc.y = 0
        self.calc.operator = '*'
        self.assertEqual(self.calc.calculation(), 0)

    def test_div(self):
        self.calc.x = 5
        self.calc.y = 3
        self.calc.operator = '/'
        self.assertEqual(self.calc.calculation(), 5/3)


class CalculatorErrorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_wrong_operator(self):
        self.calc.x = 10
        self.calc.y = 5
        self.calc.operator = 'wrong'
        self.assertFalse(self.calc.validate_operator())

    def test_divide_by_zero(self):
        self.calc.x = 10
        self.calc.y = 0
        self.calc.operator = '/'
        self.assertEqual(self.calc.calculation(), "You can't divide by 0!")

    def test_wrong_first_num(self):
        self.calc.x = "wrong_num"
        self.calc.y = 5
        self.calc.operator = '+'
        self.assertFalse(self.calc.user_input(), "Invalid number input")

    def test_wrong_second_num(self):
        self.calc.x = 10
        self.calc.y = "wrong_num"
        self.calc.operator = '+'
        self.assertFalse(self.calc.user_input(), "Invalid number input")


if __name__ == '__main__':
    unittest.main()


def run():
    return None