# Get two numbers from the user
num1 = float(input("Enter the first number: ")) # runtime: input needs to be float, not string
num2 = float(input("Enter the second number: ")) # runtime: input needs to be float, not string

# Perform multiplication
result = num1 * num2 # syntax: x is not the correct symbol for multiply
print("The product of the number is: " + str(result)) # runtime: result needs to be string, not int

# Perform division, if possible
if num2 != 0: # syntax: no variable named num logic: needs to divide negative numbers
    result = num1 / num2 # syntax: : is not the correct symbol for division
    print(f"The division of the numbers id: {result}") # syntax: result needs to be in {}
else:
    print("Division not possible: Cannot divide by zero!") 