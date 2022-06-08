class Name:
    name = "Mary"

    def __init__(self, nameless: str, age: int) -> None:
        self.name = nameless
        self.age = age


object_one = Name("Mercy", 12)
# object_two = Name()


print("Name:", object_one.name, "\nAge: ", object_one.age)
