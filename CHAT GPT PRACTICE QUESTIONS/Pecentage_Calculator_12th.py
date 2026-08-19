print()

name = input("Heyy Buddy Whats Your Name : ")

print()
print(f"Good Evening , {name}")

print()

wantness = input("Do You Want Us To Find Your Percentage ? (Y/N) : ").upper()

print()

if wantness == 'Y':
    print(f"Awesome, So {name} , Enter Your Subject Wise Marks Below !!")
   
    print()

    a = float(input("Enter Your Maths Number : "))

    b = float(input("Enter Your Physics Number : "))

    c = float(input("Enter Your Chemistry Number : "))

    d = float(input("Enter Your English Number : "))

    e = float(input("Enter Your Physical Education Number : "))


    percentage = ((a + b + c + d + e )/500)*100

    print()
    print(f"Your Percentage Is {percentage} %")
    print()
else:
 print("Oops, Its Okay")
