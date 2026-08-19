a = ("Daksh","Parv","Narendra","Archana",5,2.36,False,"Avaneesh","Harshil","Shreyansh",5,"Daksh",2.36)
print(a)

print()        




# 1) 'Count' : ye bata dega ki vo chiz kitni baar aaya hai !!

a = ("Daksh","Parv","Narendra","Archana",4,5,2.36,False,"Avaneesh","Harshil","Shreyansh",5,"Daksh",2.36)

print(a.count(2.36))
print(a.count("Daksh"))

print(a.count("Parv"))
print(a.count(4))

print(a.count(45))


print()        




# 2) 'Index' : ye bata dega ki jo type kara hai aapne uska index kya hai aur jo do baar aaya hai uska pehla index bata dega !! 

a = ("Daksh","Parv","Narendra","Archana",4,5,2.36,False,"Avaneesh","Harshil","Shreyansh",5,"Daksh",2.36)

print(a.index(2.36))
print(a.index("Daksh"))

print(a.index("Parv"))
print(a.index(4))

print()        




# 3) 'Unpacking' : ye khol deta hai tuple ko !!

my_tuple = (1,3,5,7,9,11,13,15,17)
a, b, c, d, e, f, g, h, i = my_tuple
print(a, b, c, d, e, f, g, h, i)

print()        




# 4) 'Membership' : ye bata dega ki vo word exist karta hai ya nahi !!

my_tuple = (1,3,5,7,9,11,13,15,17)
print(5 in my_tuple)
print(6 in my_tuple)

print()        




# 5) 'Repetition' : ye repeat kar dega jitni baar karana chaho !

my_tuple = (1,3,5,7,9,11,13,15,17)
repeated = my_tuple * 3    # ye 3 likha hai iska mtlb 3 baar repeat karo !!
print(repeated)

print()        




# 6) 'Concatenated' : ye tuples ko add kar deta hai 

tuple1 = (1,2,3,4,5,6,7,8,9,10)
tuple2 = (11,12,13,14,15,16,17,18,19,20)

concatenated = tuple1 + tuple2
print(concatenated)