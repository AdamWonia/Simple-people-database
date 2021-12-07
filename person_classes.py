from control_input import input_str, input_int
import time
from tkinter import filedialog as fd
import os


class Person:
    def __init__(self):
        self.name = "name"
        self.surname = "surname"
        self.age = 0
        self.gender = "gender"

    def __str__(self):
        return f"{self.name}"

    def _get_person_details(self):
        """ Method allows to insert the basic person details (name, surname, age, gender). """
        print("Insert name: ")
        self.name = input_str().strip()
        print("Insert surname: ")
        self.surname = input_str().strip()
        print("Insert age: ")
        self.age = input_int()
        print("Insert gender [M or F]: ")
        self.gender = input_str('M', 'F').strip()

    def _show_person_details(self):
        """ Method shows the person details. """
        print("Name: " + self.name)
        print("Surname: " + self.surname)
        print("Age: " + str(self.age))
        print("Gender: " + self.gender)

    def _save_details_to_file(self, save_option, data_to_write):
        """ Method allows to save the person details into chosen directory. """
        # Choosing directory:
        try:
            chosen_path = fd.askdirectory()
            if chosen_path == '':
                raise FileNotFoundError
            print("Chosen path: " + chosen_path + "\n")
            # Create person folder in chosen directory:
            person_dir = self.name + " " + self.surname
            person_dir_path = chosen_path + "/" + person_dir
            # Create folder and file.txt if not exist:
            if not os.path.isdir(person_dir_path):
                os.makedirs(person_dir_path)
                file_path = person_dir_path + "/person_details.txt"
                f = open(file_path, "w")
                # Insert person details into file:
                for data in data_to_write:
                    f.write(data + "\n")
                print("Folder: '" + person_dir + "' and file 'person_details.txt' created!")
                f.close()
            else:
                # Choose what to do if folder exists
                print("Folder exist! Do you want to overwrite it? [Y or N]")
                print("If you select 'N' a folder with a suffix of '_' will be created")
                folder_option = input_str('Y', 'N')
                # Override data in folder option:
                if folder_option == 'Y':
                    # Remove all files in path:
                    file_list = os.listdir(person_dir_path)
                    for element in file_list:
                        os.remove(person_dir_path + "/" + element)
                    # Delete existing folder after cleaning it:
                    os.rmdir(person_dir_path)
                    # Create new folder with person details:
                    os.makedirs(person_dir_path)
                    # Create folder and file.txt:
                    file_path = person_dir_path + "/person_details.txt"
                    f = open(file_path, "w")
                    # Insert person details into file:
                    for data in data_to_write:
                        f.write(data + "\n")

                    print("Folder: '" + person_dir + "' and file 'person_details.txt' created!")
                    f.close()
                    exit()
                # Otherwise create folder with suffix:
                if folder_option == 'N':
                    # Create folder with suffix '_' and file.txt:
                    look_path = os.path.dirname(person_dir_path)
                    list_files = os.listdir(look_path)
                    # Find a specific folder name and add a suffix to its name:
                    for act_dir in list_files:
                        if act_dir == person_dir:
                            person_dir_path = look_path + "/" + act_dir + '_'

                    os.makedirs(person_dir_path)
                    file_path = person_dir_path + "/person_details.txt"
                    f = open(file_path, "w")
                    # Insert person details into file:
                    for data in data_to_write:
                        f.write(data + "\n")

                    print("Folder: '" + os.path.basename(
                        person_dir_path) + "' and file 'person_details.txt' created!")
                    f.close()
        except FileNotFoundError:
            print("File not found, please try again")


class Employee(Person):
    def __init__(self):
        super().__init__()
        self.position = "position"
        self.specialization = "specialization"

    def __str__(self):
        return "Employee"

    def get_employee_details(self):
        """ Method allows to insert the employee details (name, surname, age, gender, position, specialization). """
        super()._get_person_details()
        print("Insert position: ")
        self.position = input_str().strip()
        print("Insert specialization: ")
        self.specialization = input_str().strip()

    def show_employee_details(self):
        """ Method shows the employee details. """
        super()._show_person_details()
        print("Position: " + self.position)
        print("Specialization: " + self.specialization)

    def save_employee_to_file(self, save_option):
        """ Method allows to save the employee details into chosen directory. """
        data_to_write = [f"Person: {Employee.__str__(self)}", f"Name: {self.name}", f"Surname: {self.surname}",
                         f"Age: {str(self.age)}",
                         f"Gender: {self.gender}", f"Position: {self.position}",
                         f"Specialization: {self.specialization}"]
        super()._save_details_to_file(save_option, data_to_write)


class Student(Person):
    def __init__(self):
        super().__init__()
        self.education_stage = "education stage"
        self.favourite_subject = "favourite subject"
        self.passion = "passion"

    def __str__(self):
        return "Student"

    def get_student_detail(self):
        """ Method allows to insert the student details (name, surname, age, gender, education stage
        favourite subject, passion). """
        super()._get_person_details()
        print("Insert education stage: ")
        self.education_stage = input_str().strip()
        print("Insert favourite subject: ")
        self.favourite_subject = input_str().strip()
        print("Insert passion: ")
        self.passion = input_str().strip()

    def show_student_details(self):
        """ Method shows the student details. """
        super()._show_person_details()
        print("Education stage: " + self.education_stage)
        print("Favourite subject: " + self.favourite_subject)
        print("Passion: " + self.passion)

    def save_student_to_file(self, save_option):
        """ Method allows to save the student details into chosen directory. """
        data_to_write = [f"Person: {Student.__str__(self)}", f"Name: {self.name}", f"Surname: {self.surname}",
                         f"Age: {str(self.age)}",
                         f"Gender: {self.gender}", f"Education stage: {self.education_stage}",
                         f"Favourite subject: {self.favourite_subject}", f"Passion: {self.passion}"]
        super()._save_details_to_file(save_option, data_to_write)


class Child(Person):
    def __init__(self):
        super().__init__()
        self.favourite_toy = "favourite toy"
        self.favourite_fable = "favourite fable"

    def __str__(self):
        return f"{self.name}"

    def get_child_details(self):
        """ Method allows to insert the student details (name, surname, age, gender, favourite toy, favourite fable).
        """
        super()._get_person_details()
        print("Insert favourite toy: ")
        self.favourite_toy = input_str().strip()
        print("Insert favourite fable: ")
        self.favourite_fable = input_str().strip()

    def show_child_details(self):
        """ Method shows the child details. """
        super()._show_person_details()
        print("Favourite toy: " + self.favourite_toy)
        print("Favourite fable: " + self.favourite_fable)

    def save_child_to_file(self, save_option):
        """ Method allows to save the child details into chosen directory. """
        data_to_write = [f"Person: {Child.__str__(self)}", f"Name: {self.name}", f"Surname: {self.surname}",
                         f"Age: {str(self.age)}", f"Gender: {self.gender}",
                         f"Favourite toy: {self.favourite_toy}", f"Favourite fable: {self.favourite_toy}"]
        super()._save_details_to_file(save_option, data_to_write)
