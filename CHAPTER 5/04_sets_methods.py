# Sets can have list, tuple, string, and dictionary as elements. But they cannot have mutable elements like list and dictionary as elements.
s = {1,2,3,4,5, "Daksh", "Parv", "Samanvay", 1,2,3,4,5,6,7,8,9,10}
print(s)

s.add(256)
print(s, type(s))

print(len(s))


# The difference between remove() and pop() is that remove() removes the specified element from the set, while pop() removes and returns an arbitrary element from the set. If the set is empty, pop() raises a KeyError.
s.remove(256)
print(s)

s.pop()
print(s)


s.clear()
print(s)