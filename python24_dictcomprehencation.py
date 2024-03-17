# Dictionery comprehencation 

#here similar to list comprehencation in python  

dict1= {}
for i in range(1,20):
   dict1[i]=i
print(dict1)

#by using dictionery comprehencation in pythoion  
dict2={x:x**2 for x  in range(1,20) if x%2==0}
print(dict2)