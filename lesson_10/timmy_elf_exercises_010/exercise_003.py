 # Composition vs inheritance

# Inheritance:
class Person: # 1.
    def __init__(self, street_name, postal_code, country):
        self.street_name = street_name
        self.postal_code = postal_code
        self.country = country

class Employee(Person): # 2.
    def __init__(self, street_name, postal_code, country, emp_number, salary):
        super().__init__(street_name, postal_code, country)
        self.emp_number = emp_number
        self.salary = salary

    def __str__(self):
        return f"emp {self.emp_number} live on {self.street_name}"

emp = Employee("Sveavägen", "11350", "Sweden", 1, 10000)
print(emp)

# Composition:
class Address:
    def __init__(self, street_name, postal_code, coutnry):
        self.street_name = street_name
        self.postal_code = postal_code
        self.country = coutnry

class Employee:
    def __init__(self, address, emp_number, salary):
        self.address = address
        self.emp_number = emp_number
        self.salary = salary

    def __str__(self):
        return f"emp {self.emp_number} live on {self.address.street_name}"

address = Address("Sveavägen", "11350", "Sweden")
emp = Employee(address, 1, 10000)
print(emp)