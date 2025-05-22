class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Ahmed", 50000, "123-45-6789")
print(emp.name)       # Public
print(emp._salary)    # Protected (Accessible, but not recommended)
# print(emp.__ssn)    # Private (Will raise AttributeError)
print(emp._Employee__ssn)  # Access with name mangling
