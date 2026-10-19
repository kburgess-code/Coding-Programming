

num1 = int(input("Enter your FIRST number: "))
op = input("Enter your OPERATION: ")
num2 = int(input("Enter your SECOND number: "))

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif op == "/":
    print(f"{num1} / {num2} = {num1 / num2}")

else:
    print("INVALID OPERATION")