class User:
    def __init__(self, name, age, phone, phone_code):
        self.name = name
        self.age = age
        self.phone = phone
        self.phone_code = phone_code

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone_code + self.phone)


class Manager(User):
    def print_details(self):
        super().print_details()
        print("Type", "Manager")


class Engineer(User):
    def print_details(self):
        super().print_details()
        print("Type", "Engineer")



manager = Manager("John", 25, "9379992", "050")
manager.print_details()
engineer = Engineer("Alex", 25, "9123566", "030")
engineer.print_details()