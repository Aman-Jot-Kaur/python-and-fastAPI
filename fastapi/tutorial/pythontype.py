def add(fname: str | None, lastname: str = "LASTame"):  # gave default value to lastname

    return fname + " " + lastname.title()


class Person:
    def __init__(self, name: str):
        self.name = name


name = "ak"
lasts = "jot"
result = add(name, lasts)


print(result)


def get_person_name(person: Person):
    return person.name


print(add("aman"))

