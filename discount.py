#program for discount

def disc(p):
    return p*0.9

def reg(rp):
    return rp*0.95

price=int(input("Price of the product: "))
print("Total amount of new customer: ",disc(price))
print("Total amount of regular customer: ",reg(disc(price)))
