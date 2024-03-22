n=5
for i in range(n):
    for _ in range(2):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(2*i):
            print("*",end=" ")
        print()

"""
    * *
    * *
  * * * *
  * * * *
* * * * * *
* * * * * *
"""

