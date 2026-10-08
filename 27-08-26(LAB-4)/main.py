
from university.student import student_details
from university.result import percentage_calculator

student_details("Alok", "MCA")
marks = [85, 90, 78, 88]
percentage = percentage_calculator(marks)
print(f"Percentage: {percentage}")