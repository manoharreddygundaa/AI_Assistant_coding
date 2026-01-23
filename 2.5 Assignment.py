def calculate_even_odd_sum(numbers):
    even_sum = sum(n for n in numbers if n % 2 == 0)
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return even_sum, odd_sum

nums = [1, 2, 3, 4, 5, 6]
even, odd = calculate_even_odd_sum(nums)

print("Even Sum:", even)
print("Odd Sum:", odd)
