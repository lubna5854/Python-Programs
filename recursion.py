# program to find discount, recursion

def disc(p):
    return p*0.9
def reg(rp):
    return rp*0.95
p=int(input("Enter the price"))
print("Total amount of new customer: ",disc(p))
print("Total amount of regular customer: ",disc(reg(p)))