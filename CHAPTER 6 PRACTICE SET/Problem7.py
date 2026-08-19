post = input("Enter your post: ")

# Method 1 --> Checking for all the possible cases of the string "Harry" in the post
if("Harry" in post or "harry" in post or "HARRY" in post):
    print("This post is talking about Harry.")
else:
    print("This is not talking about Harry.")

# Method 2 --> Converting the post to lower case and then comparing it with the lower case string "harry"
if("harry" in post.lower()):
    print("This post is talking about Harry.")
else:
    print("This is not talking about Harry.")

# Method 3 --> Converting both the strings to lower case and then comparing them
if("Harry".lower() in post.lower()):
    print("This post is talking about Harry.")
else:
    print("This is not talking about Harry.")