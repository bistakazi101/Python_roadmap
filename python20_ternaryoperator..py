# ternary operator  

# there are many ways to use ternary operator 
# 1. using if else 


a, b= 20,30

print( True if a>b else False)

# 0 ternary operator nested 
print(True if a>b else True if a==b else False)


# 2 using tuple 
# it returns index 0  for false  else index 1 for true
# index 0  is false an and one is true 
# syntax((fasle ,true)[2>3] it return s false index 0
print (("The index value is 0 which is false " ,"The index value is true anbd it is true ") [a>b]) 




# 2 using dictionery 
print({True:"The value is true ", False:"The value is false "}[a>b])

# 3 using lamda function 

print((lambda x, y: True if x > y else False)(a, b))
