# a function call that call itself it is known as recursion

def fun1(i:int):
    if i==0:
        return 1  # here the factorial of 0 is to be one so the loop does not ends 
    else:
        return i*fun1(i-1)

num=fun1(5)
print(num)