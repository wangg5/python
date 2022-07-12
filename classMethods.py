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

