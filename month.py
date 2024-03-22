# for describing month

month={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"Nobvember",12:"December"}
x=int(input("Enter the value: "))
if x in month:
    print("The month is: ",month[x])
else:
    print("Invalid")