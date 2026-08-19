# try ke saath else jab hi run hoga jab try wala aap succesfully chala paaye !!

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 


else:
    print("I am inside else")