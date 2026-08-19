class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    # def getInfo():   ---> This will create error !!
        # print(f"The language is {language}. The salary is {salary}")
   
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # def greet(self):
        # print("Good Morning")

    # The aove can also be written as below if you don't want an object "self" inside it !!
    @staticmethod
    def greet():
        print("Good Moning")
        
daksh = Employee()
daksh.language = "JavaScript" # This is an instance attribute
print(daksh.salary, daksh.language)

daksh.getInfo()     # ----> This converts to Employee.getInfo(daksh) -> That's why we use "self" in defining a function !!
daksh.greet()