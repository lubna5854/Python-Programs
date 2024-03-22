# reverse from 1-10

start=1
stop=2
c=stop
for i in range(2,6):
    for j in range(start,stop):
        c-=1
        print(c,end='')
    print('')
    start=stop
    stop+=i
    c=stop

#     output

#  1
#  3 2
#  6 5 4
# 10 9 8 7
