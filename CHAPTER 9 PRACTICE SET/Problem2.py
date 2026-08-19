import random 

def game():
    print("You are playing the game....")
    print(input("Are you ready to play the game (Y/N): "))
    score = random.randint(1,62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else: 
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        # Write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score

game()