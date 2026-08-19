def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c 

a = int(input("Enter Your Number: "))
b = int(input("Enter Your Number: "))
c = int(input("Enter Your Number: "))

print(f"The greatest number among a, b and c is: {greatest(a, b, c)}")