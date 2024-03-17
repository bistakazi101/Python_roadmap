# List comprehencation in python 


# List comprehencation is effective way to cerayte the list 
# example 
list1= []
for i in range(1,100):
    list1.append(i)
print (list1)

# here by creatiing list comprehencation we can create by 
list2=[x**2 for x in range(1,50)if x%2==0]
print(list2)