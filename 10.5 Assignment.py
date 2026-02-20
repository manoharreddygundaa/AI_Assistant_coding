# def add_numbers(first_number, second_number):
#     return first_number + second_number
# print(add_numbers(10, 20))

# def divide_numbers(first_number, second_number):
#     try:
#         result = first_number / second_number
#         return result
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."
#     except TypeError:
#         return "Error: Please provide valid numeric inputs."

# print(divide_numbers(10, 0))
def calculate_total_and_average(marks_list):
    """
    Calculate the total and average of student marks.

    Parameters:
        marks_list (list): A list of numeric marks.

    Returns:
        tuple: Total marks and average marks.
    """
    total_marks = sum(marks_list)
    average_marks = total_marks / len(marks_list)
    return total_marks, average_marks


def determine_grade(average_marks):
    """
    Determine the grade based on average marks.

    Parameters:
        average_marks (float): The student's average marks.

    Returns:
        str: Grade (A, B, C, or F).
    """
    if average_marks >= 90:
        return "A"
    elif average_marks >= 75:
        return "B"
    elif average_marks >= 60:
        return "C"
    else:
        return "F"


def validate_marks(marks_list):
    """
    Validate that marks are numbers between 0 and 100.
    """
    if not marks_list:
        raise ValueError("Marks list cannot be empty.")

    for mark in marks_list:
        if not isinstance(mark, (int, float)):
            raise TypeError("All marks must be numeric values.")
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100.")


# Main Program
# marks = [78, 85, 90, 66, 88]

# try:
#     validate_marks(marks)
#     total, average = calculate_total_and_average(marks)
#     grade = determine_grade(average)

#     print(f"Total Marks: {total}")
#     print(f"Average Marks: {average:.2f}")
#     print(f"Grade: {grade}")

# except (ValueError, TypeError) as error:
#     print(f"Error: {error}")


# def factorial(n):
#     """
#     Calculate the factorial of a non-negative integer.

#     Parameters:
#         n (int): A non-negative integer whose factorial is to be calculated.

#     Returns:
#         int: The factorial of the given number.

#     Raises:
#         ValueError: If n is negative.
#         TypeError: If n is not an integer.
#     """

#     # Validate input
#     if not isinstance(n, int):
#         raise TypeError("Input must be an integer.")
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")

#     result = 1  # Initialize result to 1 (factorial base value)

#     # Multiply result by each number from 1 to n
#     for i in range(1, n + 1):
#         result *= i

#     return result  # Return the final factorial value
# print(factorial(2))
def validate_password(password):
    """
    Validate a password based on multiple security rules.

    Rules:
    - Minimum length of 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character

    Parameters:
        password (str): The password entered by the user.

    Returns:
        str: Validation result message.
    """

    # Check minimum length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Flags to track required character types
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(not char.isalnum() for char in password)

    # Validate all conditions
    if not has_uppercase:
        return "Weak: Include at least one uppercase letter."
    if not has_lowercase:
        return "Weak: Include at least one lowercase letter."
    if not has_digit:
        return "Weak: Include at least one digit."
    if not has_special_char:
        return "Weak: Include at least one special character."

    return "Strong: Password meets all security requirements."


# Main Program
user_password = input("Enter password: ")
result = validate_password(user_password)
print(result)