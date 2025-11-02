# Get numbers from the user
numbers_input = input("Enter numbers with spaces: ")

# Convert input into a list of integers
numbers = [int(x) for x in numbers_input.split()]

# Display the original list
print(f"\nOriginal list: {numbers}")

# 1️ Find sum and average
total = sum(numbers)
average = total / len(numbers)
print(f"Sum: {total}")
print(f"Average: {average}")

# 2️ Find max and min
maximum = max(numbers)
minimum = min(numbers)
print(f"Max: {maximum}, Min: {minimum}")

# 3️ Remove duplicates
unique_numbers = list(set(numbers))
print(f"List without duplicates: {unique_numbers}")

# 4️ Sort ascending and descending
ascending = sorted(unique_numbers)
descending = sorted(unique_numbers, reverse=True)
print(f"Ascending order: {ascending}")
print(f"Descending order: {descending}")

# 5️ Filter even and odd numbers
even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
