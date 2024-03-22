# Read the number of students' records
n = int(input())

# Create a dictionary to store student records
student_records = {}

# Read and store student records
for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    student_records[name] = marks

# Read the name of the student to query
query_name = input()

# Calculate the average marks for the queried student
marks = student_records[query_name]
average_marks = sum(marks) / len(marks)

# Print the average marks with 2 decimal places
print("{:.2f}".format(average_marks))
