# here map is used to modify items c=ompare to filter 
print("Map function")

def fun1(value1):
    return value1*2

num= range(10)

# here in map function we cahange the values in here 
mapfun= list(map(fun1,num))
print(mapfun)