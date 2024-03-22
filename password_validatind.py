import re
def password_validation(password):
    if len(password)<10:
        return "Invalid"

    if(
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password) and
        any(char.islower() for char in password) and
        re.search(r'[!@#$%^&*().,?\"|{}<>]',password)
      ):
        return "Strong"
    else:
        return "Weak"

password=input("Enter password: ")
result=password_validation(password)
if result=="Strong":
    print("Strong")
else:
    print("Weak")

"""OUTPUT
Enter password: asasASDF23454!@
Strong"""