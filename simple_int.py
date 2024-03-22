# calculate simple interest

def simp(a,b,c):
    return ((a*b*c)/100)
p=int(input("Enter the amount: "))
n=int(input("Enter the year: "))
r=int(input("Enter the interest rate: "))
print("simple interest:",simp(p,n,r))