sub1 = int(input("Enter Subject 1 Marks: "))
sub2 = int(input("Enter Subject 2 Marks: "))
sub3 = int(input("Enter Subject 3 Marks: "))
sub4 = int(input("Enter Subject 4 Marks: "))

# Checking for total percentage
total_marks = sub1 + sub2 + sub3 + sub4
percentage = (total_marks / 400) * 100

print(f"Total Marks: {total_marks}, Percentage: {percentage:.2f}%")


# Checking for grade based on marks of Subject 1
if(90 <= sub1 <= 100):
    print("Grade: Ex")
elif(80 <= sub1 < 90):
    print("Grade: A")
elif(70 <= sub1 < 80):
    print("Grade: B")
elif(60 <= sub1 < 70):
    print("Grade: C")
elif(50 <= sub1 < 60):
    print("Grade: D")
else:
    print("Grade: E")


# Checking for grade based on marks of Subject 2
if(90 <= sub2 <= 100):
    print("Grade: Ex")
elif(80 <= sub2 < 90):
    print("Grade: A")
elif(70 <= sub2 < 80):
    print("Grade: B")
elif(60 <= sub2 < 70):
    print("Grade: C")
elif(50 <= sub2 < 60):
    print("Grade: D")
else:
    print("Grade: E")

# Checking for grade based on marks of Subject 3
if(90 <= sub3 <= 100):
    print("Grade: Ex")
elif(80 <= sub3 < 90):
    print("Grade: A")
elif(70 <= sub3 < 80):
    print("Grade: B")
elif(60 <= sub3 < 70):
    print("Grade: C")
elif(50 <= sub3 < 60):
    print("Grade: D")
else:
    print("Grade: E")

# Checking for grade based on marks of Subject 4
if(90 <= sub4 <= 100):
    print("Grade: Ex")
elif(80 <= sub4 < 90):
    print("Grade: A")
elif(70 <= sub4 < 80):
    print("Grade: B")
elif(60 <= sub4 < 70):
    print("Grade: C")
elif(50 <= sub4 < 60):
    print("Grade: D")
else:
    print("Grade: E")


print("\nThank you for using this program. Have a nice day!") 