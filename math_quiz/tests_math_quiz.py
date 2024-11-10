import unittest
from math_quiz import generate_random_integer, get_random_operator, evaluate_expression


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if the operator generated is one of the expected values
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Generate a large number of operators
            operator = get_random_operator()
            self.assertIn(operator, operators)

    def test_evaluate_expression(self):
        # Define test cases with format: (num1, num2, operator, expected_problem, expected_answer)
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 5, '+', '10 + 5', 15),
            (10, 5, '-', '10 - 5', 5),
            (10, 5, '*', '10 * 5', 50),
            (-3, 4, '+', '-3 + 4', 1),
            (-3, 4, '-', '-3 - 4', -7),
            (-3, 4, '*', '-3 * 4', -12)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = evaluate_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
