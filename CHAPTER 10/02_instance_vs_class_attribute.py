# Instance attribute take preference over class attribute

class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000


daksh = Employee()
daksh.language = "JavaScript" # This is an instance attribute
print(daksh.salary, daksh.language)
