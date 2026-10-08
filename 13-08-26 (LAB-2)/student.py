students=[("Suresh", 85), ("Mahesh", 72), ("Princy", 91), ("Roshin", 78)]
students=sorted(students, key=lambda x: x[1], reverse=True)
print(students)