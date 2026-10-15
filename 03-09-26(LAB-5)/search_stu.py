roll_search=input("Enter roll number to search: ")
with open("student.txt","r") as file:
    for line in file:
        roll, name, course, marks = line.strip().split(",")
        if roll==roll_search:
            print("\n-----Student Details-----")
            print(f"Roll Number: {roll}")
            print(f"Name: {name}")
            print(f"Course: {course}")
            print(f"Marks: {marks}")
            print(line)
            break
    else:
        print("Student not found.")
#copy one file to another file 
with open("student.txt","r") as source:
    content=source.read()
with open("student_records.txt","w") as destination:
    destination.write(content)
print("backup created successfully in student_records.txt")

#append operation
roll_search=input("Enter roll number to append: ")
with open("student.txt","a") as file:
    for line in file:
        roll, name, course, marks = line.strip().split(",")
        if roll==roll_search:
            print("\n-----Student Details-----")
            print(f"Roll Number: {roll}")
            print(f"Name: {name}")
            print(f"Course: {course}")
            print(f"Marks: {marks}")
            print(line)
            break
    else:
        print("Student not found.")