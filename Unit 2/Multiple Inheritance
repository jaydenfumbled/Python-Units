class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, dept):
        super().__init__(name, age, emp_id, salary)
        self.dept = dept

    def display(self):
        print(self.name, self.dept)


m = Manager("Jay", 18, 101, 50000, "AI")
m.display()
