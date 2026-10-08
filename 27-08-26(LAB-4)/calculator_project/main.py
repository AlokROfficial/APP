import calculator
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
print("\nAddition:", calculator.add(a,b))
print("Subtraction:", calculator.subtract(a,b))
print("Multiplication:", calculator.multiply(a,b))
print("Division:", calculator.divide(a,b))
print("Power:", calculator.power(a,b))
print("Square Root of", a, ":", calculator.square_root(a))