#Employee_Management
class Employee():
    # Created an Employee base class
    def __init__(self, name, base_salary):
        # Initialized the class constructor, with attributes of name, base_salary
        self.name = name # Instance Variable
        self.base_salary = base_salary # Instance Variable

    def calculate_salary(self):
        #Parent class method calculate_salary created for polymorphism
        pass  # Enforcing method implementation in subclasses

class RegularEmployee(Employee):
    #Child class of RegularEmployee from parent class Employee
    def __init__(self, name, base_salary, bonus):
        # Initialized the class constructor, with attributes of name, base_salary, bonus
        Employee.__init__(self, name, base_salary)
        #Explicitly calling parent constructor
        self.bonus = bonus # Instance Variable bonus

    def calculate_salary(self):
        # Child class method calculate_salary created for polymorphism
        return self.base_salary + self.bonus
        #calculation done and return the value

class ContractEmployee(Employee):
    #Child class of ContractEmployee from parent class Employee
    def __init__(self, name, hourly_rate, hours_worked):
        # Initialized the class constructor, with attributes of name, hourly_rate, hours_worked
        Employee.__init__(self, name, hourly_rate * hours_worked)
        # Explicitly calling parent constructor
        self.hourly_rate = hourly_rate # Instance Variable
        self.hours_worked = hours_worked # Instance Variable

    def calculate_salary(self):
        # Child class method calculate_salary created for polymorphism
        return self.hourly_rate * self.hours_worked
        #calculation done and return the value

class Manager(Employee):
    def __init__(self, name, base_salary, performance_bonus):
        # Initialized the class constructor, base_salary, performance_bonus
        Employee.__init__(self, name, base_salary)
        # Explicitly calling parent constructor
        self.performance_bonus = performance_bonus # Instance Variable

    def calculate_salary(self):
        # Child class method calculate_salary created for polymorphism
        return self.base_salary + self.performance_bonus
        #calculation done and return the value

# Input Values
regular_emp = RegularEmployee("Alice", 50000, 5000)
contract_emp = ContractEmployee("Bob", 1000, 160)
manager_emp = Manager("Charlie", 70000, 10000)
regular_emp1 = RegularEmployee("John", 40000, 7000)
contract_emp1 = ContractEmployee("Jeni", 2000, 120)
manager2 = Manager("Sam", 90000, 18000)


#Print the values
print("Input Values - Set1")
print(f"{regular_emp.name}'s Salary: {regular_emp.calculate_salary()}")
print(f"{contract_emp.name}'s Salary: {contract_emp.calculate_salary()}")
print(f"{manager_emp.name}'s Salary: {manager_emp.calculate_salary()}")

print("Input Values - Set2")
print(f"{regular_emp1.name}'s Salary: {regular_emp.calculate_salary()}")
print(f"{contract_emp1.name}'s Salary: {contract_emp.calculate_salary()}")
print(f"{manager2.name}'s Salary: {manager_emp.calculate_salary()}")
