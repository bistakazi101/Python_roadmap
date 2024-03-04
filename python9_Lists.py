# python Lists
# There are two types of creating a alist 
# They are
# first) square braces


# here list can be changed which means can be mutable
my_list= [1,2,3,4,5,6]
print(my_list)
my_list[0]=100
print(my_list[0])

# create using constructor list() method
my_list1= list("Sagar")
print("The list using constructor list() method",my_list1)

# append() method is used to append value to the list
print("append value ois used to append value of the list",my_list1.append("thapa"))
print(my_list1)

# extend keyword is used to extend the values
print("the extend keyword is used to extend the values",my_list1.extend([1,2]))
print(my_list1)

# insert keyword is used to insert text 
print("It is used to insert the key value pair",my_list1.insert(1,"Thapa"))
print(my_list1)

# remove() removes the first occurance of the elements
print("remove thye first occurance of the keyword",my_list1.remove("Thapa"))
print(my_list1)

# pop elements
print("pop the first elements",my_list1.pop())
print(my_list1)

# index( of the first occurance of the elements
print("Return the first index of the elements",my_list1.index(1))


# count returns the method of the count 
print("returns the number of the occurance of specified element",my_list1.count('a'))

# 3 sort() method used to sort the elements
#print("The elements is used for sorting",my_list1.sort())

 #reverse() method 
print("reverse the lists",my_list1.reverse())
print(my_list1)
 
 
 
 