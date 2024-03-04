# sequence data type
# It is snon mutable
string= "My name is sagar"
print("The string data type is non mutable data type",string)

print(type(string))
print(string[0])
# print last character of the string 
print(string[-1])

# String methods
# 1) len() method it returns the length of the string
print("The length of string",len(string))

# upper method() it is used to convert to uppwer case

print("The upper case of the string", string.upper())

# Lower method() it is used to convert to lower case
print("The lower case of the string is ", string.lower())

# capatlize method() converts the first character into the upper case
print("The capitalize of the string is ", string.capitalize())


# title method() it converts the each character to the upper case

print("The title of the string is ",string.title())

# strip method 
mycountry= "Nepal is a beautiful country "
print("the strip method is sused to strip ",mycountry.strip())

# # replace method() 
mycountryname = "I love Nepal"
print("The replace method is used to replace words:", mycountryname.replace("Nepal", "India"))


# # find() method 
mycountry = "I love Nepal"
print("The find method is used to find the index of 'Nepal':", mycountry.find("love"))


#count method() returns of the substring number of the string 
print("The count method string is used to count",string.count("My"))

# startswith   returns true or false
print("the value starts with ",string.startswith("My"))

# endswith returns of the specific suffix
print("The value of ends with ",string.endswith("sagar"))

# isalpha() checks if the valueis alpha()
# here it contains spaces not pure alphabet
print("the values is all apphabet", string.isalpha())


# isdigit() the value is digit 
# if all digits are true then returns true 
print("the value of the digit",string.isdigit())

# isspace
# if all the character of the string are whitespaces
print("The valueof the string is ",string.myspace())

# is alphanumeric()
print("the valuer of the alpha numeric", string.isalnum())


# join items
words_list = ["and", "my", "last", "name", "is", "bista"]
result = " ".join(words_list)
print("The value of the items:", result)


# idex items()
print("The value of the index items ",string.index("My"))

