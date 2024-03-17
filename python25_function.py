# python function 

# function with arguments 

def fun1(x:int ,name:list):
    print(f"The num {x} created list of{name} ")
    
fun1(1,[1,2,3,4,5])




def fun2(x ,y):
    sum= x+y
    return(x+y)

value= fun2(10,20)
print(value)


# in python i can return more than one variable

def fun3(x,y):
    return (x+y,x-y)


value1,value2= fun3(10,20)
print(f"value of sum is {value1} and value of sub is {value2}")


# nested function 
def fun4():
    def show():
        print("Show the inner function")
    show()
    print("Display the outer function")
    
fun4()