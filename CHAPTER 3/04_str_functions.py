# 1) Length Of A Word 

Name = "Daksh"
print(len(Name))


# 2) Ends With Trur OR False

Name = "Daksh"
print(Name.endswith("ksh"))
print(Name.endswith("ash"))


# 3) Starts With Trur OR False

Nmae = "Daksh"
print(Name.startswith("Da"))
print(Name.startswith("Dk"))


# 4) Capitalize Your First Word

Name = "daksh"
print(Name.capitalize())


# 5) Capitalize First Letter Of Each Word

Name = "daksh is a very good boy . parv is also a good boy but sometimes he misbehaves very much which irritates every family member that is narendra kumar kahndelwal , archana gupta , daksh kahndelwal , parv khandelwal"
print(Name.title())


# 6) Lowercase Your Word

Name = "DAKSH"
print(Name.lower())


# 7) Upercase Your Word

Name = "daksh"
print(Name.upper())


# 8) Swap Lower To Upper And Vice-Versa

Name = "dAKSH"
print(Name.swapcase())


# 9) Counts How Many Times A Word Repeats

Name = "Daksh Khandelwal"
print(Name.count("D"))
print(Name.count("d"))
print(Name.count("a"))
print(Name.count("A"))
print(Name.count("k"))
print(Name.count("s"))
print(Name.count("h"))


# 10) To Find From Where The Letters Given Are Starting From

Name = "Daksh Khandelwal"
print(Name.find("sh"))  # 3 se start ho raha to Output = 3 !!
print(Name.find("wal"))  # 13 se start ho raha to Output = 13 !!
print(Name.find("az"))  # INVALID so Output = -1 !!  (-1 matlab INVALID)


# 11) To Replace Old Word To New Word

Name = "Parv is very good good boy"
print(Name.replace("good","bad"))

Name = "Harry"
print(Name.replace("H","M"))

Name = "Daksh"
print(Name.replace("D","H").replace("k","r"))