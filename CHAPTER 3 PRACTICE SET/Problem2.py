# Method 1

a = input("Heyy Mate, Whats Your Name : " )
b = input("Whats The Date Today : ")

letter = '''Dear <|Name|>
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", a).replace("<|Date|>", b))


# Method 2 
 
birthday = '''Dear <|Name|>
Happy Birthday !!
<|Date|>''' 

print(birthday.replace("<|Name|>", "Parv Khandelwal").replace("<|Date|>", "25/08/2025"))
