sub1 = int(input("Enter Subject 1 Marks: "))
sub2 = int(input("Enter Subject 2 Marks: "))
sub3 = int(input("Enter Subject 3 Marks: "))

# Checking for total percentage
total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100

if(percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print(f"Total Marks: {total_marks}, Percentage: {percentage:.2f}%, Result: Pass")
else:
    print(f"Total Marks: {total_marks}, Percentage: {percentage:.2f}%, Result: Fail")