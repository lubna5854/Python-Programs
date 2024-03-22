# write a python code to open a file named filepgm.txt and write some random data into it

#Create a text file

file=open("filepgm.txt",'w')
file.write("Hello welcome")
file.close()

#adding lines using write method

file=open("filepgm.txt",'a')
file.write("\n This is added line")
file.close()

#read the file and print the content

file=open("filepgm.txt",'r')
cont=file.read()
print("The file contents: ",cont)
file.close()

#readline concept

file=open("filepgm.txt",'r')
cont=file.readline()
print("The line: ",cont)
file.close()

#to read particular line, first 15 letters, space consider as a letter

file=open("filepgm.txt",'r')
con=file.read(15)
print("Specified line: ",con)
file.close()