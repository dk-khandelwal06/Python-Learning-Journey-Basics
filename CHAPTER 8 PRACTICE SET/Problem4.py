'''
sum(1) = 1
sum(2) = 1 + 2 = 3
sum(3) = 1 + 2 + 3 = 6
sum(4) = 1 + 2 + 3 + 4 = 10
sum(5) = 1 + 2 + 3 + 4 + 5 = 15

sum(n) = 1 + 2 + 3 + 4 + ............ + n-1 + n

'''

def sum_of_n(n):
    if (n == 0 or n < 0):
        return "This number is not a natural number"
    elif (n == 1):
        return 1
    return sum_of_n(n-1) + n

n = int(input("Enter a Number: "))
print(f"The sum of {n} natural number is: {sum_of_n(n)}")
