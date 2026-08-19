# Agar sab kuch bhula ke exit karna hai to break ka use karte hai. Break statement loop ko turant rok deta hai aur control ko loop ke bahar le jata hai.

for i in range(100):
    if i == 34:
        break  # Exit the loop when i is 34
    print(i)

print()

# Agar kisi specific condition ke liye loop ko skip karna hai to continue ka use kar
# Matlab ye hai ki 34 tak to chalao yaani 33 tak likho but jo 34 hai usko skip kar do aur 35 se continue karo.

for i in range(100):
    if i == 34:
        continue  # Skip the rest of the loop when i is 34
    print(i)

# Note: Break statement is used to exit the loop when a certain condition is met, while continue statement is used to skip the current iteration and move to the next iteration of the loop.


# Very Very Important: In first one print statement is after the if condition and in second one print statement is before the if condition. So, in first one 34 is not printed but in second one 34 is printed.
for i in range(100):
    if i == 34:
        break  # Exit the loop when i is 34
    print(i)

print()

for i in range(100):
    print(i)

    if i == 34:
        break  # Exit the loop when i is 34