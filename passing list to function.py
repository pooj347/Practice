def add_numbers(num1, num2, num3):
    """
    This function takes three numbers as arguments and prints their sum.
    """
    print(f"The sum is: {num1 + num2 + num3}")

# Create a list of numbers
numbers = [10, 20, 30]

# Call the function and unpack the list
add_numbers(*numbers)
