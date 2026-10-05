print("Calculator")
math = input("Enter a math operation (+, -, *, /): ")
if math == "+":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print("The result is:", result)
elif math == "-":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print("The result is:", result)
elif math == "*":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print("The result is:", result)
elif math == "/":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("The result is:", result)
else:
    print("Invalid operation")