import random
from typing import Union
from typing import Literal
from typing import Tuple

def generate_random_integer(min_value: int, max_value: int) -> int:
    """
    Generate a random integer within a specified range.

    Parameters
    ----------
    min_value : int
        The minimum value of the random integer.
    max_value : int
        The maximum value of the random integer.

    Returns
    -------
    int
        A random integer between `min_value` and `max_value`, inclusive.

    Raises
    ------
    ValueError
        If `min_value` is greater than `max_value`.
    TypeError
        If `min_value` or `max_value` is not an integer.
    """
    # Check if inputs are valid types
    if not isinstance(min_value, int) or not isinstance(max_value, int):
        raise TypeError("Both min_value and max_value should be integers.")

    # Check for logical value error
    if min_value > max_value:
        raise ValueError("min_value should not be greater than max_value.")

    try:
        # Attempt to generate and return a random integer within the given range
        return random.randint(min_value, max_value)
    except ValueError as e:
        # Catch any unforeseen ValueError from random.randint and re-raise with a custom message
        raise ValueError(f"An error occurred when generating a random integer: {e}")


def get_random_operator() -> Literal['+', '-', '*']:
    """
    Select a random mathematical operator from a predefined set.

    Returns
    -------
    Literal['+', '-', '*']
        A randomly chosen operator, either '+', '-', or '*'.
    """
    try:
        # Select a random operator from the list and return it
        return random.choice(['+', '-', '*'])
    except IndexError as e:
        # Catch any unforeseen IndexError from random.choice and re-raise with a custom message
        raise IndexError(f"An error occurred when selecting a random operator: {e}")


def evaluate_expression(n1: int, n2: int, operator: str) -> Tuple[str, int]:
    """
    Evaluate a mathematical expression based on two integers and an operator,
    returning both the formatted expression and the result.

    Parameters
    ----------
    n1 : int
        The first integer in the expression.
    n2 : int
        The second integer in the expression.
    operator : str
        The operator for the expression, expected to be one of '+', '-', or '*'.

    Returns
    -------
    Tuple[str, int]
        A tuple containing:
        - str: A string representation of the expression (e.g., "5 + 3").
        - int: The result of the calculation.
    """
    # Construct the expression string
    expression = f"{n1} {operator} {n2}"

    # Perform the calculation based on the operator
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    else:  # operator == '*'
        result = n1 * n2

    return expression, result


def math_quiz():
    """
    Conduct a math quiz where the user answers a series of random math problems.

    The game generates random math questions using addition, subtraction, or
    multiplication, and checks the user's answers to calculate a score.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Prints the user's score after completing the quiz.
    """
    score = 0
    total_questions = 3  # Setting the total number of questions to an integer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random integers and an operator for the math question
        n1 = generate_random_integer(1, 10)
        n2 = generate_random_integer(1, 5)
        operator = get_random_operator()

        # Get the formatted problem and correct answer
        problem, answer = evaluate_expression(n1, n2, operator)

        # Display the question to the user
        print(f"\nQuestion: {problem}")

        # Get the user's answer
        user_input = input("Your answer: ")

        # Check if the input is a valid integer and matches the answer
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            user_answer = int(user_input)
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        else:
            print("Invalid input! Treating as a wrong answer.")
            print(f"The correct answer is {answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
