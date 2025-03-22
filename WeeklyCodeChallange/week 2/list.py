
# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

def get_sum():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    total = sum(numbers)
    print(f"The sum is: {total}")

get_sum()
