

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name is {self.name}"

    def __eq__(self, other):
        return self.name == other.name and other.age == self.age


p1 = Person("Mary", 18)
p2 = Person("Mary", 18)

print(p1 == p2)
