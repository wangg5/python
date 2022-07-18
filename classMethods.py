"""
https://www.youtube.com/watch?v=rq8cL2XMM5M
"""

class Person:
    def __init__(self, name):
        self.name = name

    def info(age):
        if age < 20:
            return "teens"
        elif age < 50:
            return "mid age"
        elif age < 70:
            return "elderly"
        else:
            return "senior"
print(Person.info(40))
Joe = Person("Joe")
# can not call Joe.info(20)
# But, we can do this

class PersonII:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def info(age):
        if age < 20:
            return "teens"
        elif age < 50:
            return "mid age"
        elif age < 70:
            return "elderly"
        else:
            return "senior"
Joe = PersonII("Joe")
print(Joe.info(18))
print("class: \n ", PersonII.info(80))



"""
    class methods
"""
class PersonIII:
    industry = "Computer Science"
    def __init__(self, name):
        self.name = name

    @classmethod
    def info(cls, age):
        print(f"industry is {cls.industry}")
        if age < 20:
            return "teens"
        elif age < 50:
            return "mid age"
        elif age < 70:
            return "elderly"
        else:
            return "senior"

Max = PersonIII("Max")

print(Max.info(18))
print("using class name access class method: \n", PersonIII.info(18))







