# class sru_student:
#     def __init__(self, name, roll_no, hostel_status):
#         self.name = name
#         self.roll_no = roll_no
#         self.hostel_status = hostel_status
#         self.fee = None  # Initially fee is not updated

#     def fee_update(self, amount):
#         self.fee = amount

#     def display_details(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)
#         print("Hostel Status:", self.hostel_status)
#         print("Fee:", self.fee if self.fee is not None else "Not Updated")
# student1 = sru_student("Manohar", 101, "Yes")
# student1.fee_update(50000)
# student1.display_details()


# class sru_student:
#     """
#     A class representing a student with name, roll number, and hostel status.
#     """

#     def __init__(self, name, roll_no, hostel_status):
#         """
#         Initializes the student with name, roll number, and hostel status.
#         """

#     def fee_update(self, amount):
#         """
#         Updates the student's fee.
#         """

#     def display_details(self):
#         """
#         Prints the student's details.
#         """





def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters
    ----------
    a : number
        The first value.
    b : number
        The second value.

    Returns
    -------
    number
        The result of adding a and b.
    """
def add(a, b):
    """Add two numbers.

    Parameters
    ----------
    a : int or float
    b : int or float

    Returns
    -------
    int or float
        Sum of a and b.
    """
    return a + b
def divide(a, b):
    """Divide two numbers.

    Parameters
    ----------
    a : int or float
    b : int or float

    Returns
    -------
    float

    Raises
    ------
    ZeroDivisionError
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
