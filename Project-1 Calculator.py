# python program to create a simple calculator

# 3 steps to create a simple calculator
# 1. functions for operations
# 2. user input
# 3. display results

# 1. functions for operations
# function to add two numbers
def add(num1, num2):
    return num1 + num2

# function to subtract two numbers
def sub(num1,num2):
    return num1 -num2

# function to multiply two numbers
def mul(num1, num2):
    return num1*num2

# function to divide two numbers
def div(num1, num2):
    return num1/num2

# function to find average of two numbers
def avg(num1, num2):
    return (num1 + num2)/2

# step -2 user input

print (" please select operation to perform \n" \
        "1. Addition\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Average\n")

select = int(input("Select operation from 1 to 5: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# step -3 display results

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", mul(num1,num2))
elif select == 4:
    print(num1, "/", num2, "=", div(num1,num2))
elif select == 5:
    print("Average of", num1, "and", num2, "is", avg(num1,num2))
else:
    print("Invalid input, please select operation from 1 to 5")
# end of program