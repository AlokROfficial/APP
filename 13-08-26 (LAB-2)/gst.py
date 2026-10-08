from functools import reduce
p=list(map(int,input("Enter product prices: ").split()))\
p_gst=list(map(lambda x: x*0.18, p))
f_p=list(lambda x: x>500, p_gst)
total=reduce(lambda x,y: x+y, f_p,0)