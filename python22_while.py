# while loop 
print("Print the while loop ")
num= 0
while(num<=5):
    print(num)
    num+=1
    
    
    # here python does not have do while loop 
    
print("Terminate loop with break \
    statemensts ")
num = 0  # Initialize num


# here break statements terminate sinnn  3
while(num <= 5):
    print(num)
    num += 1
    if(num == 3):
       break
   
# continue statements is used to terminate the currennt ststenments and execute \ next itteration  or skipps 
num =0
while num<=5:
    num+=1
    # here 3 is skipped 
    if num==3:
        continue
    print(num)  
# pass keyword 
# pass keyword is used for empty string 
def function1(x:int):
    pass
# hwere pass will do nothing 
function1(100)