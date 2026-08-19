try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:  # Aise hi ham kisi aur error ka bhi change kar sakte hai !!
    print("Heyyyy")
    print(v)

except Exception as e:
    print(e)

print("Thank You")