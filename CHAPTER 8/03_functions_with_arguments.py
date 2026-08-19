def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)

goodDay("Daksh", "Thank You")
goodDay("Parv", "Thanks")
goodDay("Khushi", "Thanks Daksh") 
goodDay("Narendra", "धन्यवाद")
goodDay("Archana", "Dhanyawaad")

# Return

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"  # Function tu ek value le ke jaa jo bhi variable maange use de dena !!

a = goodDay("Daksh", "Thank You")
print(a)