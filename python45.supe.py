class A:
    def __init__(self):
        print("A class constructor")
        self.varname = "sagar"
        
    def display(self):
        print("Display method of A class")
        # in inheritance python always search for sdeapth first search 
class B():
    def __init__(self):
        self.A_instance = A()
        super().__init__
        print(self.A_instance.varname)  # Access varname attribute of A_instance
        print("B class constructor")
        self.varname = "Bista"
        
obj1 = B()
