class Number: 
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return self.n / other.n

    def __floordiv__(self, other):
        return self.n // other.n

    def __str__(self):
        return str(self.n)

    def __len__(self):
        return len(self.n)

n = Number(10)
m = Number(5)

print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n // m)

name = Number("Daksh")
print(len(name))

f = Number(3.14)
print(str(f))