# alphabet pyramid pattern

size = int(input("Enter the limit : "))
alpha = 65  # ASCII value of A

for i in range(size):
    # print spaces
    for j in range(size - i):
        print(" ", end=" ")
    # print alphabets
    for k in range(2 * i + 1):
        print(chr(alpha + k), end=" ")
    print()

 #    Output
 #     A
 #    ABC
 #   ABCDE
 #  ABCDEFG
 # ABCDEFGHI
