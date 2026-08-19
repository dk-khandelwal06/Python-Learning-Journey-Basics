# Detect ke liye "find" wala string function use karenge 

Name = "Daksh  Khandelwal  is  a  very  good  boy  !!"
print(Name.find("  "))  # Output = 5 yaani 'Double Space' hai to sahi 

Name = "Daksh Khandelwal is a very good boy !!"
print(Name.find("  "))  # Output = -1 yaani 'Double Space' hai hi nahi 