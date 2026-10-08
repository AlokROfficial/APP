def performance(*marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade


name = input("Enter student name: ")
course = input("Enter subjects: ")

marks = list(map(float, input("Enter marks: ").split()))

percentage, grade = performance(*marks)

print("\nStudent Name:", name)
print("Course:", course)
print("Percentage:", percentage)
print("Grade:", grade)