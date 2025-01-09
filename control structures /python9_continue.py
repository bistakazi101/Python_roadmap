"""the continue ittereate the next loop and continue the flow of the structure """

max= input("Enter the max value ;")
for i in range(int(max)):
    if i%2:
      continue
    print(f"the value of i is : {i}")