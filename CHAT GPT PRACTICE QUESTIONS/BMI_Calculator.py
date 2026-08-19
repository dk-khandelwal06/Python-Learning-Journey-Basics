# Ques.) BMI Calculator !!

print()
name = input("Heyy Mate Enter Your Name : ")
print()

print(f"Good Afternoon {name} !!")
print()

want = input(f"So, {name} Do You Want Us To Know Your BMI Or Not (Y/N) : ").strip().upper()

if want== 'Y':
    print()
    weight = float(input(f"So, {name} Enter Your Weight in 'kg' : "))
    print()
    height = float(input(f"So, {name} Enter Your Height in 'm' : "))
    print()
    formula = [weight / (height)**2]
    print(f"So, {name} Your BMI is : ",formula)
    print()
else:
    print()
    print(f"Okay {name} Its Okay , You Enjoy !!")    

print()