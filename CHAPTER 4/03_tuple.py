# ye list hai !!  ------ "MUTABLE"

a = ["Daksh","Parv","Narendra","Archana",5,2.36,False,"Avaneesh","Harshil","Shreyansh"]
print(type(a))


# ye tuple hai !!  ------ "IMMUTABLE" 

b = ("Daksh","Parv","Narendra","Archana",5,2.36,False,"Avaneesh","Harshil","Shreyansh")
print(type(b))


c =(1)
print(type(c))       # -------- Integer Type

c =(1,)
print(type(c))       # -------- Tuple Type     (comma{,} lagana jaruri hai)



# Example Of Tuple Immutability 

d = ("Daksh","Parv","Narendra","Archana",5,2.36,False,"Avaneesh","Harshil","Shreyansh")
# d[5]= 3.69
# print(d)       ------------ ERROR !!
