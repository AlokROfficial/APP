    
#sum of n numbers 
def sum_of_n(n):
    if n==0:
        return 0
    else:
        return n+sum_of_n(n-1)
    
print(f"sum is {sum_of_n(5)} of first 5 numbers")  