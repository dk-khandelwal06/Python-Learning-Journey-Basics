class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000


daksh = Employee()
daksh.name = "Daksh" # This is an instance attribute
print(daksh.name, daksh.salary, daksh.language)

parv = Employee()
parv.name = "Parv Roro Robinson"
print(parv.name, parv.language, parv.salary)

# Here name is instance attribute and salary and language are class attribute as they directly belongs to class