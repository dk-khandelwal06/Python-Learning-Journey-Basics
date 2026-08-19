import random

# Snake = 1
# Water = -1
# Gun = 0

computer = random.choice([-1, 0, 1])

youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

youstr = input("Enter your choice (s/w/g): ").lower()
you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a Draw!")

elif (computer - you == -1) or (computer - you == 2):
    print("You Lose!")

else:
    print("You Win!")