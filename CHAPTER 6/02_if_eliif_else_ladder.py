a = int(input("Enter your age: "))

# If elif else ladder to check voting eligibility

if(a >= 18):
    print("You are eligible to vote.")

elif(a < 0):
    print("Invalid age entered. Age cannot be negative.")

elif(a == 0):
    print("You are not eligible to vote as you are a newborn.")

else: 
    print("You are not eligible to vote.") 


# This line will always be executed regardless of the condition beacause it is outside the if-elif-else ladder
print("\nThank you for using the voting eligibility checker.\nHave a great day!")