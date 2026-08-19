# Ques) Ek number input lo aur uska square aur cube print karo.

print()
a = float(input("Enter Your Number : "))

print()
b = input("Do You Want Us To Sqaure Your Number OR Cube Your Number ? (S/C) : ").upper()

print()
if b == 'S':
    print(f"""Awesome, 
             The Square Of Your Number Is : {a**2}""")
elif b == 'C':
    print(f"""Awesome,
             The Cube Of Your Number Is : {a**3}""") 
else:
    print("Ohh!! Its Okay")        
print()