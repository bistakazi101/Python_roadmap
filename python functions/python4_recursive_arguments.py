"a recursive function is function that calls itself untill it doesnot"
def countdown(start):
     print(start)
     next= start-1
     if next>0:
         countdown(next)
  
# Start the countdown from 10
countdown(10)
