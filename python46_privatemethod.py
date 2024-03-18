class myclass:
    myname= "sagar"
    def __init__(self):
        self.__private_method()  # Calling the private method within the constructor
        self._name="sagar"

    def __private_method(self):  # Define a private method
        self.varname = "sagar"
        print("private method ", self.varname)
        print(self.myname)


class subclass(myclass):
    def __init__(self):
        print("Rhe procted value is insccesible  ")
        print("Subclass constructor")
obj1 = myclass()
