import random

computer = random.choice(["Rock","Paper","Scissor"])
your = input("Enter Your Choice: ")
yourchoice = your.capitalize()
print(f"Your Choice is {yourchoice} \nComputer Choice is {computer}")

if(computer == yourchoice):
    print("It's a Draw !!")
elif(computer == "Rock" and yourchoice == "Paper"):
    print("You Win !!")
elif(computer == "Rock" and yourchoice == "Scissor"):
    print("You Lose !!")
elif(computer == "Paper" and yourchoice == "Rock"):
    print("You Win !!")
elif(computer == "Paper" and yourchoice == "Scissor"):
    print("You Lose !!")
elif(computer == "Scissor" and yourchoice == "Paper"):
    print("You Win !!")
elif(computer == "Scissor" and yourchoice == "Rock"):
    print("You Lose !!")
else: 
    print("Something went wrong !!")