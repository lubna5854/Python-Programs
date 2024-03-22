n = int(input("Enter number of students: "))
result = {}
total_highest=[]
math_highest=0
phy_highest=0
eng_highest=0
for i in range(n):
    print("Enter Details of student No.", i+1)
    rno = int(input("Roll No: "))
    name = input("Name: ")
    maths = int(input("maths : "))
    phy=int(input("Physics: "))
    English=int(input("English: "))
    total=maths+English+phy
    result[rno] = {'name': name, 'maths': maths, 'physics': phy, 'english': English, 'total': total}
    total_highest.append((name,total))
    if maths>math_highest:
        math_highest=maths
        math_high_student=(rno,math_highest)
    if phy>phy_highest:
        phy_highest=phy
        phy_high_student=(rno,phy_highest)
    if English>eng_highest:
        eng_highest=English
        eng_high_student=(rno,eng_highest)

highest=max(total_highest)
print("Highest: ",highest)
print("Maths highest: ",math_high_student)
print("Physics highest: ",phy_high_student)
print("English: ",eng_high_student)
sorted_result=sorted(result.items(),key=lambda x:x[1]['total'],reverse=True)
for rno, details in sorted_result:
    print(f"\nRoll No: {rno}")
    print("Name:", details['name'])
    print("Maths:", details['maths'])
    print("Physics:", details['physics'])
    print("English:", details['english'])
    print("Total Marks:", details['total'])

del_record=input("Do u want to delete any record? If yes enter the roll number, else type No: ")
if del_record=="No":
    pass
else:
    del_record=int(del_record)
    if del_record in result:
        print("Record deleted..!")
        result.pop(del_record)
    else:
        print("Invalid..")
