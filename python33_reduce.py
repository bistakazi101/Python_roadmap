    # here reduce function only returns a single value 
import functools
    # here we have to use functools in order to use treduce method 
    

def fun1(a, b):
    return a + b

num1 = range(0,10)  # Change range to start from 1 to avoid multiplying by 0

# Use functools.reduce() to apply fun1() cumulatively to the items of num1
result = functools.reduce(fun1, num1)

print("Result:", result)
