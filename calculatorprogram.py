first = int(input("Enter first number: "))
operator = input("Enter operator: ")
second = int(input("Enter second number: "))

if operator == "+":
    print("The answer is",first + second)
elif operator == "-":
    print("The answer is",first - second)
elif operator == "*":
    print("The answer is",first * second)
elif operator == "/":
    print("The answer is",first / second)
else:
    print("invalid option")





