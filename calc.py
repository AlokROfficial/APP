a=int(input("enter a value: "))
b=int(input("enter a value: "))
i=0
while(i==0):
    print()
    print(f"1.addition")
    print(f"2.Subtraction")
    print(f"3.Multiplication")
    print(f"4.Division")
    print(f"5.Exit")
    n=int(input("Enter your choice: "))
    if n==1:
        print("added value:",a+b)
    if n==2:
            print("subtracted value:",a-b)
    if n==3:
            print("multiplied value:",a*b)
    if n==4:
            print("Division value:",a/b)
    if n==5:
            break                            