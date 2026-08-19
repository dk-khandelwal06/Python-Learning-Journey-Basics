list1 = [3,5,8,1,6,9,12,56,24,63,23,89,1,56,45,25,12,36,49,69,2,99,0]
print(list1)

list2 = ["Devi Ram Gupta","Saroj Devi","Ramji Lal Gupta","Geeta Devi","Ashok Gupta","Seema Gupta","Narendra Kumar Khandelwal","Archana Gupta","Santosh Gupta","Uma Gupta","Yogesh Khandelwal","Anima Dadhich","Narendra Kumar Khadelwal"]
print(list2)


print()        



a = (input("Hey Buddy What's Your Name : "))
print(f"Good Afternoon {a} !!")


print()        




# 1) 'Sort' : ye ascending order mein le aata hai agar numbers de rakhe ho to ya sirf words de rakhe ho !!

list1.sort()
list2.sort()

print(list1)
print(list2)

print()        



# 2) 'Reverse' : ye reverse kar dega sequence !!

list1.reverse()
list2.reverse()

print(list1)
print(list2)

print()        



# 3) 'Append' : ismein list ke last mein kuch add kar sakte hai !!

list1.append(-1)
list2.append("Daksh")

print(list1)
print(list2)

print()        



# 4) 'Insert' : insmein listke bich mein kuch add kar sakte hai to insert(konse index , kya lagana) !!

list1.insert(3,67)
list2.insert(1,"Samanway")

print(list1)
print(list2)

print()        



# 5) 'Remove' : ye jo chiz remove karni vo likh do !!

list1.remove(-1)
list2.remove("Daksh")

print(list1)
print(list2)

print()        

 

# 6) 'Pop' : ye delete kar dega vo index pe jo hai aur agar print ke liye bolo to bata bhi dega kya delete kara !!

a = list1.pop(3)
b = list2.pop(1)


print(a)
print(b)

print(list1)
print(list2)


# ye is liye laga raha hoon taaki gap aa jaaye abhi aata nahi hai to aisi hi kar raha hoon !!

print()      