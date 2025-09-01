n = int(input("enter the number to find factorial:"))

# Initialize the factorial variable to 1
fact = 1

# Calculate the factorial using a for loop
for i in range(1, n + 1):
    fact *= i

print("The factoril is:",fact)
