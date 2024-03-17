# locals and globals keyword in python 
# a symbol table is data structuure which contains all the data structure 
# the globals function returns the dictionery in the python
# the locals function returns the dictionery of the current local symbol table


# 1) globals functions it sii built in function

a=100
def demo():
    b=10
    # here locals keyword works in local scope
    print("Hellow world")
    print(locals()['b'])
    

print(globals())
demo()

# if we want to acess one specific keyword or value we have to use 
print(globals()['a'])

