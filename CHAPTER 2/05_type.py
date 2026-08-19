# Type jo hai vo bata dega ki kaunsi class hai !! (INTEGER , FLOAT , STRING)

a = 31
aa = type(a) # integer
print(aa)

b = 30.56
bb = type(b) # floating
print(bb)

c = "Daksh"
cc = type(c) # string
print(cc)

d = "38.4"
dd = type(d) # ye bhi string hi hoga kyuki "" mein hai 
print(dd)


# Conversions

e = "38.4"
ee = float(e) # e but type should be float (conversion)
eee = type(ee)
print(eee)

f = "35"
ff = int(f) # f but type should be integer (conversion)
fff = type(ff)
print(fff)

g = "Daksh"
gg = str(g) # ismein koi ERROR nahi aayega becaz it is string only
# gg = int(g) # g but type should be integer (coversion) # ERROR (INVALID)
# gg = float(g) # g but type should be float (coversion) # ERROR (INVALID)
ggg = type(gg)
print(ggg)


# Real Conversions

h = 25
hh = float(h)
print(hh)

i = 25
ii = int(i)
print(ii)

j = "25" 
jj = str(j) # ismein 25 hi output dikahyega kyuki terminal mein "" dikhta hi nahi hai !!
print(jj)

