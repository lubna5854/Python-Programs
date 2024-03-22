if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            i, e = map(int, command[1:]) # is using a technique called "unpacking" along with the map function to
                                        # extract values from a list and assign them to variables i and e.
            my_list.insert(i, e)
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            e = int(command[1])
            my_list.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            my_list.append(e)
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "reverse":
            my_list.reverse()
