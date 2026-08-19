def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e) 
        return

    finally: # Saare niyam todte hue chalta hai !!
        print("Hey I am inside of finally")

    print("Hello Guruji")
    # Dekho tum soch sakte ho finally na bhi lagaon chalega par samjho jaise upar return kar diya apan ne to simple print("") likhte to nahi hota print par yahan finally wala print ho jaayega !!
    
main()