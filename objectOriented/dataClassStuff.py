from dataclasses import dataclass


@dataclass(order=True)
class Person:
    name: str
    age: int
    children: []

    def is_minor(self):
        return self.age < 18


person_one = Person("Mary", 12, ["Mike", 'Asa'])
person_two = Person("Mary", 42, ["Hosea"])

print(person_one)
