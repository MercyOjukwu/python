user_access_details = [
    {"username": "Mary", "password": "1234pass"},
    {"username": "Jonathan", "password": "funmi123"},
    {"username": "Wills", "password": "123goaway"}

]


access_details = {
    "favorite food": ["fish", "meat", "snail"],
    "favorite players": {"Barca": "Suarez", "Chelsea": "Lukaku"},
    "favorite girl": "Funke",
    "favorite music": ["shine shine", "go away"]
}

contact_details = {
    "full name": "Mary Okon",
    "phone number": ["08023574500"],
    "school": ["Semicolon", "Cisca"]
}


def lst_checker(username, password):
    for user in user_access_details:
        if user["username"] == username and user["password"] == password:
            return True
        return False


def type_checker(typ):
    for value in access_details.values():
        if type(value) == typ:
            print(True)


def add_phone_no(new_number):
    for key, value in contact_details.items():
        if key == "phone number" and type(value) == list:
            value.append(new_number)


if __name__ == "__main__":
    add_phone_no("12345")
    print(contact_details)
