# static methoid 
# Three types of methods in python
# 1. Instance method
# 2. Class method
# 3. Static method

# Static method is the method which is not related to the class or instance of the class
# it is made for externbal data purpose 

class bank:
    bank_name="Nepal bank"
    r=8.2
    @staticmethod
    # static method is same like class method but it is not related to the class or instance
    def simplest_method(p,t):
        print(int(p*t*bank.r)/100)
        
        
obj1= bank()
obj1.simplest_method(1000,2)
        