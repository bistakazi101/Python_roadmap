# Types of arguments in python 


# positional arguments 
def fun1(x,y):
    return x+y

value= fun1(3,5)
print(value)


# keyword arguments 
# The keyword arguments are in name and pair value of like positional arguments 


def fun21(name,classno):
    print(f"name is {name} and class is class is {classno}")
    
    
fun21(name="sagar",classno=10)



# default arguments 
# The default arguments are the default value of the function

def fun4(name ,classno=10):
    print(f"The name is {name } and class is {classno}")
    
fun4("sagar",12)
fun4("Ram")