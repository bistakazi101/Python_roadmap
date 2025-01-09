"""python doc string """
print(help(print))


def sum(x,y):
    """This function returns two numbers """
    return x+y
print(help(sum))

print(sum.__doc__)