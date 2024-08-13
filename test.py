import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Random Numbers:", random_numbers)

# Filter out even numbers
odd_numbers = [num for num in random_numbers if num % 2 != 0]

print("Odd Numbers:", odd_numbers)

# Calculate the sum of odd numbers
odd_sum = sum(odd_numbers)

print("Sum of Odd Numbers:", odd_sum)

# A random message to show the result
if odd_sum > 100:
    print("That's a big sum!")
else:
    print("The sum is within a reasonable range.")
