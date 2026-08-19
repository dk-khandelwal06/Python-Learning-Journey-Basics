class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # Dunder Method which is automatically called
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
            print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Moning")


# To skip these boring work we use _init_ constructor !!
# daksh = Employee()
# daksh.name = "Daksh"
# print(daksh.name, daksh.salary)

rohan = Employee("Rohan", 200000, "JavaScipt")
print(rohan.name, rohan.salary, rohan.language)