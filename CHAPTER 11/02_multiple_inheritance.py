class Employee:
    name = "Default Name"
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the comapany is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()