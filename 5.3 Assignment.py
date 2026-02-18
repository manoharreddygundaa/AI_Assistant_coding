# # Simple login system (AI-generated)

# username = "admin"
# password = "admin123"

# input_username = input("Enter username: ")
# input_password = input("Enter password: ")

# if input_username == username and input_password == password:
#     print("Login successful")
# else:
#     print("Invalid credentials")


# #revised version

# import hashlib

# # Simulated secure credential storage (hashed password)
# stored_username = "admin"
# stored_password_hash = hashlib.sha256("admin123".encode()).hexdigest()

# # User input
# input_username = input("Enter username: ").strip()
# input_password = input("Enter password: ").strip()

# # Hash the entered password
# input_password_hash = hashlib.sha256(input_password.encode()).hexdigest()

# # Authentication check
# if input_username == stored_username and input_password_hash == stored_password_hash:
#     print("Login successful")
# else:
#     print("Invalid credentials")


# def loan_approval(name, gender, income, credit_score):
#     if gender == "Male" and income > 30000 and credit_score > 650:
#         return "Loan Approved"
#     elif gender == "Female" and income > 40000 and credit_score > 700:
#         return "Loan Approved"
#     else:
#         return "Loan Rejected"
# print(loan_approval("manohar", "Male", 350000 , 700))

# def loan_approval(income, credit_score):
#     if income > 35000 and credit_score > 680:
#         return "Loan Approved"
#     else:
#         return "Loan Rejected"
# def binary_search(arr, left, right, target):
#     # Base case: if the search space is exhausted
#     if left > right:
#         return -1

#     # Find the middle index
#     mid = (left + right) // 2

#     # If the target element is found at mid
#     if arr[mid] == target:
#         return mid

#     # If target is smaller, search the left half
#     elif arr[mid] > target:
#         return binary_search(arr, left, mid - 1, target)

#     # If target is larger, search the right half
#     else:
#         return binary_search(arr, mid + 1, right, target)


# # Example usage
# numbers = [2, 4, 6, 8, 10, 12, 14]
# key = 10

# result = binary_search(numbers, 0, len(numbers) - 1, key)

# if result != -1:
#     print("Element found at index:", result)
# else:
#     print("Element not found")
#
#
def employee_details(name, gender, salary):
    if gender == "Male":
        title = "Mr."
    else:
        title = "Ms."

    print(f"{title} {name} has a salary of {salary}")
employee_details("Manoharreddy","Male",1200000)

def employee_details(name, salary, title=""):
    if title:
        print(f"{title} {name} has a salary of {salary}")
    else:
        print(f"{name} has a salary of {salary}")
employee_details("Manoharreddy",1200000,"Mr")
