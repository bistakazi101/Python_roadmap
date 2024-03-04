# match and case in python
def check_value(x):
    # match is like switch case in python
    #in python iit is like c and c++ switch case type and underscore was introduced in python 3.10
    match x:
     case 1:
        print("first case")
     case 2:
        print("Second case")
     case "name":
        print ("My name is sagar")
        
        
        # (underscore is default)
     case _:
         print("The value is default")
check_value(2)
check_value("name")