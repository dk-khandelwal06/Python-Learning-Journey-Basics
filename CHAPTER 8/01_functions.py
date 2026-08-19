# If we want we can convert these many codes into functions

'''
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

average = (a + b + c)/3
print(average)

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

average = (a + b + c)/3
print(average)
'''

# Functions

# Function Definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c)/3
    print(average)

avg() # Function Call
avg()
avg()
avg()
avg()