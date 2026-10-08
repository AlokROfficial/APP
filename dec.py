#use decorator function to check whether a number is palindrome or not
def palindrome(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        str_num=str(result)
        print(str_num==str_num[::-1])
    return wrapper
@palindrome
def get_number(num):
    return num
get_number(121)