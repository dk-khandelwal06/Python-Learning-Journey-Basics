# Ques) Do number input lo aur uska addition , subtraction , multiplication , division , remainder print karo.

print()

a = float(input("Enter Your 1st Number : "))
b = float(input("Enter Your 2nd Number : "))

print()
c = input("Do You Want Us To Find Addition , Subtraction , Multiplication , Division , Remainder ? (A/S/M/D/R) : ").strip().upper()

print()
if c == 'A':
    print(f"""Awesome, 
             The Addition Of Your Numbers Is : {a + b}""")
elif c == 'S':
    print(f"""Awesome,
             The Subtraction Of Your Numbers Is : {a - b}""") 
elif c == 'M':
    print(f"""Awesome,
             The Multiplication Of Your Numbers Is : {a * b}""") 
elif c == 'D':
    if b != 0:
        print(f"""Awesome,
             The Division Of Your Numbers Is : {a / b}""")
    else:
        print("Error: Division by zero is not allowed.")     
elif c == 'R':
    if b != 0:
        print(f"""Awesome,
             The Remainder Of Your Numbers Is : {a%b}""") 
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Ohh!! Its Okay")        
print()




