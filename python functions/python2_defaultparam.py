"""python default parameters """
# def function_name(param1, param2=value2, param3=value3, ...):
def greet(name,msg="good morning"):
    return f"{name}{msg}"


print(greet("sagar"))
# here the second arguments uses instead of the second arguments 
print(greet("sagar","good night"))

# multiple default argumenst 
def greet(name="sagar",msg="good morning"):
    return f"{name}{msg}"

greet("sumit","good night")
