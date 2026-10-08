def outer(degree):
    def inner(num):
        return pow(num,1/degree)
    return inner
root_inner=outer(2)
print(root_inner(42))