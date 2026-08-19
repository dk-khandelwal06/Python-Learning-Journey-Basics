a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

# Kisi bachhe ko maarna nahi chhaiye par usko maaro taaki vo sudhre ye vahi hai error daala hai jaan bujh ke taaki sudhre aur crah ho taaki sabak mile aur aage se dhayan rakhe

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide number by zero !!")
else:
    print(f"The division a/b is {a/b}")