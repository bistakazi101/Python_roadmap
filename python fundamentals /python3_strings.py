# python string 


#double quote 
message ="my name is ssagar bista "


#single quote 
message ='my name is sagar bista'

# escape quotes 
message = 'It\'s also a valid string'
print(message)

#if you dont want to to treat backslash (\)sahen add the followings
message=r"it\'s so a valid strings "
print(message)

# use variable sin python string 

name1="sagar"
name=f"my name is {name1} bista"
print(name)

#creating multiline cursors 

help_message ="""
usage:mysql command 
-h hostname
-d database name
-u username
-p password"""


print(help_message)


#python strings concenations 
#python automatically concenates strings    
greeting ="hello" "world"
print(greeting)


# acessing string literals 
print(greeting[0])
print(greeting[-1])
print(greeting[1])


# to ge the length of the string 
print(len(greeting))


#slicing the string
string="hello world"
print(string[0:5])


# note python string are immutable 
# string[0]="H" this will give error
# to change the string you have to create new string
string ="h"+string[1:]
print(string)