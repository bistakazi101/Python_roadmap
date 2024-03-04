# Tuple in python allow duplicate values
# it is non mutable which means read only
tuple1=(1,2,3,4,5,6) # it is of the type tuple
tuple2=("sagar","thapa",1,2,3,[1,2,3,4,5,]) # if both elements then it is type tuple

print(type(tuple1))
print(tuple1[0])
print(tuple2[0])
print(type(tuple2))

# converting list to tuple 
my_list=[1,2,3,4,5,6]
tuple1=tuple(my_list)
print(tuple1)


# acessing list 
my1=[1,2,("name","sagar",1,2)]
print(type(my1))
my1[0]=100
print(my1)