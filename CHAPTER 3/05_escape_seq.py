print()
# 1) Newline

Name = "Daksh is a very quite boy.\nBut sometimes he behave like an introvert kid.\nSpecially in front of his friends."
print(Name) 
# ab iska Method 1 to "\n" wala hai aur Method 2 hai """""" ya '''''' use kar sakte ho !!


print()
# 2) Tab

Name = "Daksh is a very quite boy.\tBut sometimes he behave like an introvert kid.\tSpecially in front of his friends."
print(Name)


print()
# 3) Single/Double QUOTE 

Name = "\"Daksh\" is a very \'quite\' boy.\n\"But\" sometimes he behave like an introvert \'kid\'.\n\"Specially\" in front of his \'friends\'."
print(Name)
# bina escape seq character ke karta to invalid ho jaata kyuki python confuse ho jayega kab "" end wala kehna chaha raha hai aur kab words ko highlight ke liye use kara hai


print()
# 4) Real Backslash

Name = "Daksh is in the \nutshell"  # ab mujhe nutshell ke pass \ lagana hai par vo to newline samjh jayega !
print(Name)

                        # SOLUTION                    
Name = "Daksh is in the \\nutshell !!"   # \\ laga diya !!
print(Name)
