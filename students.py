# write a program to accept student name and then show the respective mark

students={"Anu":320,"Amisha":450,"Varun":425,"Vishnu":487,"Samira":325,"Diya":452,"Mukthi":476,"Aisha":485,"Laya":490,"Krithika":387}
name=str(input("Enter students name :"))
if name in students:
    print("Mark: ",students[name])
else:
    print("Not valid")