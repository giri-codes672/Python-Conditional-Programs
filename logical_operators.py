# Logical Operators

# Check number range
num = int(input("Enter a number: "))

if num >= 10 and num <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")

# Check string
text = input("Enter a string: ")

if text != "" and len(text) > 5:
    print("Valid string")
else:
    print("Invalid string")
