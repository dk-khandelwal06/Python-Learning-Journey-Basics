print()
name = input("Heyy Mate, Whats Your Name : ")

print()
print(f"Good Afternoon {name} !!")

print()
want = input(f"So, {name} What Do You Want ? (°F to °C / °C to °F / K to °C / °C to K / K to °F / °F to K) ----- [C/F/K] : ").strip().upper()

if want== 'C':
    
    print()
    want_1 = input("What Do You Want Now ? (°F to °C / K to °C) ------ [FC/KC] : ").strip().upper()
    if want_1== 'FC':
        print()
        degree_F = float(input("Enter Temperature In Fahrenheit : "))
        celsius = (degree_F - 32) * (5/9)
        print()
        print(f"Temperature In Celsius : {celsius} °C")
        print()
    elif want_1== 'KC':
        print()
        degree_K = float(input("Enter Temperature In Kelvin : "))
        celsius = (degree_K -  273.15)
        print()
        print(f"Temperature In Celsius : {celsius} °C")
        print()
    else:
        print()
        print()
        print(f"Its Okay {name} Brother !!")
        print()

elif want=='F':

    print()
    want_2 = input("What Do You Want Now ? (°C to °F / K to °F) ------ [CF/KF] : ").strip().upper()
    if want_2== 'CF':
        print()
        degree_C = float(input("Enter Temperature In Celsius : "))
        fahrenheit = (degree_C * 9/5) + 32
        print()
        print(f"Temperature In Fahrenheit : {fahrenheit} °F")
        print()
    elif want_2== 'KF':
        print()
        degree_K = float(input("Enter Temperature In Kelvin : "))
        fahrenheit = (degree_K -  273.15) * (9/5) + 32
        print()
        print(f"Temperature In Fahrenheit : {fahrenheit} °F")
        print()
    else:
        print()
        print()
        print(f"Its Okay {name} Brother !!")
        print()

elif want=='K':

    print()
    want_3 = input("What Do You Want Now ? (°C to K / °F to K) ------ [CK/FK] : ").strip().upper()
    if want_3== 'CK':
        print()
        degree_C = float(input("Enter Temperature In Celsius : "))
        kelvin = (degree_C + 273.15)
        print()
        print(f"Temperature In Kelvin : {kelvin} K")
        print()
    elif want_3== 'FK':
        print()
        degree_F = float(input("Enter Temperature In Fahrenheit : "))
        kelvin = (degree_F - 32) * (5/9) + 273.15
        print()
        print(f"Temperature In Kelvin : {kelvin} K")
        print()
    else:
        print()
        print()
        print(f"Its Okay {name} Brother !!")
        print()
else:
    print()
    print()
    print(f"Its Okay {name} Brother !!")
    print()


print()
print("I Hope You Loved The Project !!")
print()
print()