# Nested class 

# wgy we need nested class?
# 1. To group classes that are only used in one place
# 2. To increase the readability of the code
# when one class object does not exists without the other class object then



class university:
    def __init__(self):
        print("This is the constructor of university class")
        
    class department:
        def __init__(self):
            print("This is the constructor of department class")
            
        def display(self):
            print("This is the display method of department class")
            
        class student:
            def __init__(self):
                print("This is the constructor of student class")
                
            def display(self):
                print("This is the display method of student class")
                
obj1= university()
obj2= university.department()
obj2.display()