print()
name = input("Enter Your Name : ")

print()
classs = input("Enter Your Class (10/12) : ")

if classs== '10':
    print()
    division = input("10th With IT / 10th Without IT ? (IT / NOT IT) : ").strip().upper()
    if division== 'IT':
        print()
        a = float(input("Enter Your Marks In Maths : "))
        b = float(input("Enter Your Marks In Science : "))
        c = float(input("Enter Your Marks In Social Studies(SST) : "))
        d = float(input("Enter Your Marks In English : "))
        e = float(input("Enter Your Marks In Hindi : "))
        f = float(input("Enter Your Marks In IT : "))
        print()

        want = input(f"So, {name} Do You Want Us To Find Your Percentage ? (Y/N) : ").strip().upper()
        if want== 'Y':
            print()
            percentage = ((a+b+c+d+e+f)*100)/600
            print(f"""Awesome, 
                So, {name} Your Percentage in 10th is : {percentage} %""")
        else:
            print(f"Its Okay {name} , Thanks For Participating In Code !!")

    elif division== 'NOT IT':
        print()  
        a = float(input("Enter Your Marks In Maths : "))
        b = float(input("Enter Your Marks In Science : "))
        c = float(input("Enter Your Marks In Social Studies (SST) : "))
        d = float(input("Enter Your Marks In English : "))
        e = float(input("Enter Your Marks In Hindi : "))
        print()

        want = input(f"So, {name} Do You Want Us To Find Your Percentage ? (Y/N) : ").strip().upper()
        if want== 'Y':
            print()
            percentage = ((a+b+c+d+e)*100)/500
            print(f"""Awesome, 
                So, {name} Your Percentage in 10th is : {percentage} %""")
        else:
            print(f"Its Okay {name} , Thanks For Participating In Code !!")
    else:
        print(f"Its Okay {name} , Thanks For Participating In Code !!")


elif classs=='12':
    print()
    division = input("12th With PCM / 12th With PCB ? (PCM / PCB) : ").strip().upper()
    if division== 'PCM':
        print()
        a = float(input("Enter Your Marks In Physics : "))
        b = float(input("Enter Your Marks In Chemistry : "))
        c = float(input("Enter Your Marks In Maths : "))
        d = float(input("Enter Your Marks In English : "))
        e = float(input("Enter Your Marks In Physical Education : "))

        want = input(f"So, {name} Do You Want Us To Find Your Percentage ? (Y/N) : ").strip().upper()
        if want== 'Y':
            print()
            percentage = ((a+b+c+d+e)*100)/500
            print(f"""Awesome, 
                So, {name} Your Percentage in 12th is : {percentage} %""")
        else:
            print(f"Its Okay {name} , Thanks For Participating In Code !!")

    elif division== 'PCB':
        print()
        a = float(input("Enter Your Marks In Physics : "))
        b = float(input("Enter Your Marks In Chemistry : "))
        c = float(input("Enter Your Marks In Biology : "))
        d = float(input("Enter Your Marks In English : "))
        e = float(input("Enter Your Marks In Physical Education : "))
        print()

        want = input(f"So, {name} Do You Want Us To Find Your Percentage ? (Y/N) : ").strip().upper()
        if want== 'Y':
            print()
            percentage = ((a+b+c+d+e)*100)/500
            print(f"""Awesome, 
                So, {name} Your Percentage in 12th is : {percentage} %""")
        else:
            print(f"Its Okay {name} , Thanks For Participating In Code !!")

else:
    print()
    print(f"Its Okay {name} , Thanks For Participating In Code !!")
    print()

print()
print(f"Thanks For Participating In My Code {name} !!")
print()