s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 

print(s)
print(len(s))

# We thought that the length of s would be 3, but it is actually 2. This is because 20 and 20.0 are considered equal in Python, so only one of them is added to the set. The string '20' is a different data type, so it is added to the set as well. Therefore, the length of s is 2.

# Example 
print(20 == 20.0)
