# Given an integer,n , and n space-separated integers as input, create a tuple, t, of those  n integers. Then compute and print the result of hash(t) .
#
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
#
# Input Format
#
# The first line contains an integer,n , denoting the number of elements in the tuple.
# The second line contains n space-separated integers describing the elements in tuple t .

if __name__ == '__main__':
    n = int(input())  # Read the number of elements
    integer_list = map(int, input().split())  # Read and convert space-separated integers to a list

    # Create a tuple from the list of integers
    t = tuple(integer_list)

    # Compute and print the hash of the tuple
    print(hash(t))

# output
# input as
# 2
# 1 2
# output will be
# 3713081631934410656
