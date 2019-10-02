"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token


from arithmetic import *


# Your code goes here

while True:
    token = input(":") 
    token = token.split(" ")

    operator = token[0]

    if operator == "q":
        quit()

    num1 = float(token[1])
    num2 = float(token[2])

    

    if operator == "+":
        answer = add(num1, num2) 

    elif operator == "-":
        answer = subtract(num1, num2)

    elif operator == "*":
        answer = multiply(num1, num2)

    elif operator == "/":
        answer = divide(num1, num2)
        
    #dont forget the loop
    print(answer)
