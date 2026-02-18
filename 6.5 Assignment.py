# age = int(input("Enter your age: "))
# citizen = input("Are you a citizen? (yes/no): ")

# if age >= 18 and citizen.lower() == "yes":
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
