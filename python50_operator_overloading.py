# operator overloading in python 



class myclass:
    a=10
    b=20
    c=a+b
    print(a+b)
    
    # this will also print to smme value in python 
    print(a.__add__(b))
    
    print(int.__add__(a,b))
    print(dir(a))
    
    
    def __init__(self,title,pages):
        self.title= title
        self.pages= pages
        
        
    def __add__(self,other):
        return self.pages+other.pages
    
    
b1= myclass("sagar",100)
b2= myclass("sagar",200)
print ("total number of pages", b1+b2)
