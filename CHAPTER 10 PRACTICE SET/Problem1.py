class Programmer():
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name 
        self.salary = salary
        self.pin = pin

p = Programmer("Daksh",120000,302021)
print(p.name, p.salary, p.pin)

r = Programmer("Rohan",100000,304021)
print(r.name, r.salary, r.pin)