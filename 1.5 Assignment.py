#reverse a string without function
string = input("Enter a string: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print("Reversed string:", reversed_string)
#optimized code 
text = input("Enter a string: ")
print(text[::-1])
#using functions
def reverse_string(text):
    return text[::-1]

user_input = input("Enter a string: ")
result = reverse_string(user_input)
print("Reversed string:", result)


#Loop-Based Approach
text = input("Enter a string: ")
rev = ""

for ch in text:
    rev = ch + rev

print(rev)

#Built-in / Slicing Approach

text = input("Enter a string: ")
print(text[::-1])
