marks=list(map(int,input("enter marks separately: ").split()))
update=list(map(lambda x: min(x+5,100),marks))
print("original marks",marks)
print("Updated marks",update)