n=5
for i in range(n):
    for j in range(n - i):
        print(" ", end=' ')
    for k in range(2 * i - 1):
        print("*", end=' ')
    print()

for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(2*(n-i)+1):
        print("*",end=" ")
    print()

#     OUTPUT
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

"""
# reverse pyramid pattern
n=5
for i in range(1,n+1):
    for j in range(i-1):
        print(' ', end=' ')
    for k in range(2*(n-i)+1):
        print("*", end=' ')
    print()

#   OUTPUT
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
"""

"""
# right pascal triangle
n=5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

# OUTPUT
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

"""

"""
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

# OUTPUT
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

"""
"""
# downward triangle star pattern
n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

#     output

# * * * * *
#   * * * *
#     * * *
#       * *
#         *
"""
"""
# right triangle star pattern

for i in range(5):
    for j in range(5 - i-1):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()

#     output
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
"""
"""
# Left triangle star pattern


for i in range(5):
    # internal loop run for i times
    for k in range(i+1):
        print("*", end=" ")
    print()

#     output

* 
* * 
* * * 
* * * * 
* * * * * 
"""

"""
# downward triangle star pattern
n = 5

for i in range(n):
    # internal loop run for n - i times
    for j in range(n - i):
        print('*', end=' ')
    print()

#     output

#   * * * * *
#   * * * *
#   * * *
#   * *
#   *
"""

"""
# plus pattern
n=5
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
"""
output
    *     
    *     
* * * * * 
    *     
    *   
"""
"""
n=5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

output

*       * 
  *   *   
    *     
  *   *   
*       * 
"""