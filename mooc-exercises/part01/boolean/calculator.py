# Write your solution here
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
oper = input("Operation: ")

print()

if oper == "add":
    print(f"{num1} + {num2} = {num1 + num2}")

elif oper == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")

elif oper == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")
