"""python break """

value= input("Enter the value  : ")
for i in range(int(value)):
    if i == 5:
        print("you entered 5")
        # here i sthe value ois 5 so we are breaking the loop
        print("breaking the loop")
        break   
    print(f"Iteration {i}: Value is not 5")

