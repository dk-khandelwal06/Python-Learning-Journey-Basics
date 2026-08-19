from random import randint 

n = randint(1,100)

a = -1
guesses = 0
while(a != n):
    a = int(input("Guess the Number: "))
    if (a > n): 
        print("Lower Number Please !!")
        guesses += 1
    elif(a<n): 
        print("Higher Number Please !!")  
        guesses += 1

print(f"You have guessed the number {n} in {guesses} attempts")