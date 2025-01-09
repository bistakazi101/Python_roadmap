"""python lambda functions """

# we use lambda keyword for creating lambda functions
# lambda parameters: expression
sum=lambda x,y: x+y
print(sum(10,20))


#function that accepts a function as a argument 
def fun1(firstname, lastname, formatter):
    return formatter(firstname, lastname)

fullname= fun1("sagar", "bista", lambda x,y: x+" "+y)
print(fullname)

# function that returns  the lambda function 

def fun2(firstname, lastname):
    print(f"The first name and lastname is {firstname} and lastname is{lastname}")
    return lambda firstname,lastname:firstname+" "+lastname

sum= fun2("sagar",'bista1')
print(sum("sagar1","bista2"))