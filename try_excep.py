# write a function which would devide two numbers, design the function in a manner that it handles
# the divide by zero exception

try:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("Division: ",x/y)
except:
    print("Invalid")
