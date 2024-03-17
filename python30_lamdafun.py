# lamda function 
# a lamda function is a small anonymous function.
# 1) does not return function

add= lambda x: print("Hellow world")
add("Hellow my name si sagar")


# 20lambda function returning function 

add= lambda x: x+100
print(add(10))


# 3)lambda function returning lambda function 
add= lambda x: lambda y:x+y
add1= add(10)

print(add1(10))

# iffe immediately invoked function 
result= (lambda x:x+100)(10)
print(result)