name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Phone number: "))

s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

t = "The name of the student is {0}, his phone number is {2} and marks are {1}".format(name, marks, phone)

print(s)
print(t)