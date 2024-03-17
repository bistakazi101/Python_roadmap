# passing function as a parameter
# we can pass function in the python



# returning function and passing function 
def display(show):  #Formal arguments 
   return show()



def show():
    return('Passing function as a argument in show function')

value=display(show) #actual arguments 
print(value)