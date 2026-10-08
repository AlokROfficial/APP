from student_result import calculate_total
from student_result import calculate_percentage
from student_result import calculate_grade
n=int(input("Enter the number: "))
marks=[]
for i in range(n):
    roll=input(f"Enter roll number for subject {i+1}: ")
    name=input(f"Enter name for subject {i+1}: ")
    course=input(f"Enter course for subject {i+1}: ")
    mark=float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total=calculate_total(marks) 
percentage=calculate_percentage(marks)
grade=calculate_grade(percentage)
print("\n-----Student Result-----")
print("Marks",marks)
print("Total",total)
print("Percentage",round(percentage,2))
print("Grade",grade)
