# Write your solution here
fahr = float(input("Please type in a temperature (F): "))

cels = (fahr - 32) / 1.8

print(f"{fahr} degrees Fahrenheit equals {cels} degrees Celsius")

if cels < 0:
    print("Brr! It's cold in here!")
