
#inputing a string 
name= input("my name is :")
print(name)

value= input("please input a value: ")
#here by default is is represented as string
print("you have entered: ",value)

#example of type conversion
price= input("please input the price ")
tax= input("please input the tax (%):")

int(price)
int(tax)

tax_amount= int(price)*int(tax)/100
print(tax_amount)

print(type(price))
print(type(tax))


