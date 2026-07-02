# Comparison Operators

def compare_numbers(a, b):
    if a > b:
        print(a, "is larger than", b)
    elif b > a:
        print(b, "is larger than", a)
    else:
        print("Both numbers are equal")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

compare_numbers(num1, num2)
