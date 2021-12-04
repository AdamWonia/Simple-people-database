from functions import input_str, input_int


class Person:

    def __init__(self):
        self.name = ""
        self.surname = ""
        self.age = 0
        self.gender = ""

    def _get_person_details(self):
        """ add docstring """
        print("Insert name: ")
        self.name = input_str().strip()
        print("Insert surname: ")
        self.surname = input_str().strip()
        print("Insert age: ")
        self.age = input_int()
        print("Insert gender [M or F]: ")
        self.gender = input_str('M', 'F').strip()

    def _show_person_details(self):
        """ add docstring """
        print("Name: " + self.name)
        print("Surname: " + self.surname)
        print("Age: " + str(self.age))
        print("Gender: " + self.gender)

    def __str__(self):
        return f"{self.name}"


class Employee(Person):
    def __init__(self):
        super().__init__()
        self.position = ""
        self.specialization = ""

    def get_employee_details(self):
        """ add docstring """
        super()._get_person_details()
        print("Insert position: ")
        self.position = input_str().strip()
        print("Insert specialization: ")
        self.specialization = input_str().strip()

    def show_employee_details(self):
        """ add docstring """
        super()._show_person_details()
        print("Position: " + self.position)
        print("Specialization: " + self.specialization)


class Student(Person):
    def __init__(self):
        super().__init__()
        self.education_stage = ""
        self.favourite_subject = ""
        self.passion = ""

    def get_student_detail(self):
        """ add docstring """
        super()._get_person_details()
        print("Insert education stage: ")
        self.education_stage = input_str().strip()
        print("Insert favourite subject: ")
        self.favourite_subject = input_str().strip()
        print("Insert passion: ")
        self.passion = input_str().strip()

    def show_student_details(self):
        super()._show_person_details()
        print("Education stage: " + self.education_stage)
        print("Favourite subject: " + self.favourite_subject)
        print("Passion: " + self.passion)


class Child(Person):
    def __init__(self):
        super().__init__()
        self.favourite_toy = ""
        self.favourite_fable = ""

    def get_child_details(self):
        """ add docstring """
        super()._get_person_details()
        print("Insert favourite toy: ")
        self.favourite_toy = input_str().strip()
        print("Insert favourite fable: ")
        self.favourite_fable = input_str().strip()

    def show_child_details(self):
        """ add docstring """
        super()._show_person_details()
        print("Favourite toy: " + self.favourite_toy)
        print("Favourite fable: " + self.favourite_fable)
