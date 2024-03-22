
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
        'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'ninteen']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']


def Tens(num):
    if num <= 20:
        return ones[num - 1] if num > 0 else " "
    else:
        val1 = int(num / 10)
        val = num % 10
        return tens[val1 - 1] + " " + ones[val - 1]

def hundreds(num):
    val_hundred=int(num / 100)
    val_tens=num % 100
    result=ones[val_hundred-1] + " hundred"
    if val_tens > 0:
        result += " " + Tens(val_tens)
    return result


def thousands(num):# 54987
    val_thousand=int(num/1000) # 54
    val_hundred=num % 1000 #987
    if val_thousand>20:
        val_tens=int(val_thousand/10)# 5
        val1_tens= val_thousand % 10 # 4
        result_thousand=tens[val_tens-1] + " " + ones[val1_tens-1] + " thousand"
    else:
        result_thousand=ones[val_thousand-1] + " thousand"
    if val_hundred >0:
        result_thousand += " " + hundreds(val_hundred)
    return result_thousand


def lakhs(num):
    val_lakh=int(num/100000) # 26
    val_ten_thousand=num % 100000 # 54987
    if val_lakh > 20:
        val_ten=int(val_lakh/10) # 2
        val1_ten=val_lakh % 10 # 6
        result_lakhs = tens[val_ten-1] + " " + ones[val1_ten-1] + " lakhs"
    else:
        result_lakhs=ones[val_lakh-1] + " lakhs"
    if val_ten_thousand>0:
        result_lakhs += " " + thousands(val_ten_thousand)
    return result_lakhs


number=int(input("Enter the number: "))
if number <100:
    print(Tens(number))

elif 100 <= number < 1000:
    print(hundreds(number))

elif 1000 <= number < 100000:
    print(thousands(number))

else:
    print(lakhs(number))
