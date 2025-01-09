"""python recursive function """
def sum(a):
    if (a )>0:
        return a+ sum(a-1)
    else:
      return  0
  
sum1= sum(10)
print(sum1)