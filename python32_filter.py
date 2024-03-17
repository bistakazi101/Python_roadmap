# function which takes other function as an argument is san higher order functions
# there are three types of higher order function 
# 1)ilter functions 
# syntax filter(function_name,itterable)

def filter_fun(value1):
    return value1%2==0

numbers =range(10)
filternum= list(filter(filter_fun,numbers))
print(filternum)

#here filter object is used to only print the values  
# def greater than 10
def fun1(value1):
    if value1>5:
        print(f"The {value1} is greater than 5")
    else:
        print(f"The {value1} is less than 5")
        #in filter it is used only to store tempory value at once after print it shows null
        
num= range(10)
num1= list(filter(fun1, num))