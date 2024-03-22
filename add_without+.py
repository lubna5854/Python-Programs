def add_without_plus_operator(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Input two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 < 0 or num2 < 0:
    print("Please enter positive integers.")
else:
    result = add_without_plus_operator(num1, num2)
    print("The sum of {} and {} is: {}".format(num1, num2, result))
