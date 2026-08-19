# NO

class Demo:
    a = 4

o = Demo()
print(o.a) # Print the class attribute becaz instance attribute is not present

o.a = 0 # Instance attribute is set 
print(o.a) # Prints the instance attribute beacuse instance attribute is present
print(Demo.a) # Prints the class attribute