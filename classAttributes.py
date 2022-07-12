"""
https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
"""


class SoftwareEngineer:
    # class attributes, whole class can use it
    industry = "Computer Science"
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

se1 = SoftwareEngineer("John", 20, "L4", 5000)
se2 = SoftwareEngineer("Sophia", 25, "L5", 6000)

print(SoftwareEngineer.industry)
print(se1.industry)
print(se2.industry)
print(se1.name, se1.age, se1.level, se1.salary)
print(se2.name, se2.age, se2.level, se2.salary)


class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        # for class attributes, if you want to access them, do not 
        # use self.XXX, use class name as prefix.
        return Circle.pi*self.radius*self.radius

c1 = Circle(10)
print("area = ", c1.area())
