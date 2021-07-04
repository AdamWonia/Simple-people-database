class Person():
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def showPersonDetails(self):
        print("Name: " + self.name)
        print("Surname: " + self.surname)
        print("Age: " + str(self.age))
        print("Gender: " + self.gender)


class Employee(Person):
    def __init__(self, name, surname, age, gender, position, specialization):
        super().__init__(name, surname, age, gender)
        self.position = position
        self.specialization = specialization

    def showEmployeeDetails(self):
        super().showPersonDetails()
        print("Position: " + self.position)
        print("Specialization: " + self.specialization)


class Student(Person):
    def __init__(self, name, surname, age, gender, education_stage, fav_subject, passion):
        super().__init__(name, surname, age, gender)
        self.education_stage = education_stage
        self.fav_subject = fav_subject
        self.passion = passion

    def showStudentDetails(self):
        super().showPersonDetails()
        print("Education stage: " + self.education_stage)
        print("Favourite subject: " + self.fav_subject)
        print("Passion: " + self.passion)


class Child(Person):
    def __init__(self, name, surname, age, gender, fav_toy, fav_fable):
        super().__init__(name, surname, age, gender)
        self.fav_toy = fav_toy
        self.fav_fable = fav_fable

    def showChildDetails(self):
        super().showPersonDetails()
        print("Favourite toy: " + self.fav_toy)
        print("Favourite fable: " + self.fav_fable)
