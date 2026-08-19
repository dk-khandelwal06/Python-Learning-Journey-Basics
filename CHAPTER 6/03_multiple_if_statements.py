a = int(input("Enter your age: "))

# If statement number 1 to check if the age is an even number. It is an independent if statement and will be executed regardless of the outcome of the second if statement.
if(a % 2 == 0):
    print("Your age is an even number.")
# End of if statement number 1

# If statement number 2 to check voting eligibility
if(a >= 18):
    print("You are eligible to vote.")

elif(a < 0):
    print("Invalid age entered. Age cannot be negative.")

else: 
    print("You are not eligible to vote.") 
# End of if statement number 2

print("\nThank you for using the voting eligibility checker.\nHave a great day!")

# Note 1: The first if statement is independent of the second if statement. This means that both if statements will be executed regardless of the outcome of the other. 
# Note 2: We can have multiple independent if statements in a program. Each if statement will be executed independently of the others. But we can not have multiple elif statements without an if statement. An elif statement must always be preceded by an if statement.