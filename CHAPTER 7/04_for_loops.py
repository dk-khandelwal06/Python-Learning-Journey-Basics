# Range function is used to generate a sequence of numbers. It can take one, two, or three arguments. The most common usage is with one argument, which specifies the end of the range (exclusive). The range starts from 0 by default.
# It starts from 0 to n-1, where n is the argument passed to the range function. If two arguments are passed, it starts from the first argument and goes up to the second argument (exclusive). If three arguments are passed, the third argument specifies the step size.

for i in range(4):
    print(i)