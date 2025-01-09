"""in c it was generally called as conditin  operator """

# age = input ("please enter your age : ")
# if int(age)>=18:
#     ticketprice= 100
# else:
#     ticketprice= 50
    
# print(f"your ticket price is : {ticketprice}")    


"""if we have to write same problem then we can use ternnary operator in python """
age = input("Enter the age : ")


# syntax value_if_true if condition else value_if_false
ticketprice=100 if int(age)>=18 else 50
print(f"your ticket price is : {ticketprice}")