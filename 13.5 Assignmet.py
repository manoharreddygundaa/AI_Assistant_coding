# Legacy Code
a = [10, 20, 30, 40]

total = 0
for i in a:
    total = total + i
print("Sum:", total)

avg = 0
for i in a:
    avg = avg + i
avg = avg / len(a)
print("Average:", avg)


# Refactored Code
numbers = [10, 20, 30, 40]

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

#2 
# Legacy Code
a = [5, 10, 15]
s = 0
for x in a:
    s += x
print(s)

# Refactored Code
numbers = [5, 10, 15]
total_sum = 0

for number in numbers:
    total_sum += number

print("Total Sum:", total_sum)

#3
# Legacy Code
n = 5
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("Factorial:", fact)

# Refactored Code
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("Factorial:", factorial(5))

#4
# Legacy Code
squares = []
for i in range(1, 6):
    squares.append(i*i)

print(squares)

# Refactored Code
squares = [i*i for i in range(1,6)]
print(squares)

#5
# Legacy Code
numbers = [3, 7, 2, 9, 5]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest:", largest)

# Refactored Code
numbers = [3, 7, 2, 9, 5]
largest = max(numbers)

print("Largest:", largest)


#6
# Legacy Code
num = int(input("Enter number: "))
result = 10 / num
print(result)

# Refactored Code
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

#7
# Legacy Code
x = 10

def add():
    global x
    x = x + 5
    print(x)

add()

# Refactored Code
def add(x):
    return x + 5

result = add(10)
print(result)


# Legacy Code
numbers = [1,2,3,4,5,6,7,8,9,10]
even = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)

print(even)

# Refactored Code
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
