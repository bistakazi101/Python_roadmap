"""python elif block"""
age= input("please enter your age : ")
if int(age) <= 5:
    print("You are a kid")
elif int(age) >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    