def sum_digit(a):
    result=0
    current=0
    for char in a:
        if char.isdigit():
            current=current * 10 + int(char)
        else:
            result += current
            current=0
    result += current
    return result
a=str(input())
print(sum_digit(a))