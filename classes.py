from functions import input_str, input_int
import time
from tkinter import Tk, filedialog as fd
import os


class Person:

    def __init__(self):
        self.name = "name"
        self.surname = "surname"
        self.age = 0
        self.gender = "gender"

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
        self.position = "position"
        self.specialization = "specialization"

    def __str__(self):
        return "Employee"

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

        # Saving person details to file:
        # maybe make method save in Person?

        print("Do you want to save the person's data to a file? [Y or N]")
        save_option = input_str('Y', 'N')

    def save_details_to_file(self):
        print("Do you want to save the person's data to a file? [Y or N]")
        save_option = input_str('Y', 'N')

        if save_option == 'Y':
            print("Choose a directory to save: ")
            print("Note: A folder and file will be created with the person data")
            time.sleep(2)

            # Choosing directory:
            try:
                chosen_path = fd.askdirectory()
                if chosen_path == '':
                    raise FileNotFoundError

                print("Chosen path: " + chosen_path + "\n")
                # Create person folder in chosen directory:
                person_dir = self.name + " " + self.surname
                person_dir_path = chosen_path + "/" + person_dir

                if not os.path.isdir(person_dir_path):
                    # Create folder and file.txt:
                    os.makedirs(person_dir_path)
                    file_path = person_dir_path + "/person_details.txt"
                    f = open(file_path, "w")
                    # Insert person details into file:
                    data_to_write = [f"Person: {str(Employee)}", f"Name: {self.name}", f"Surname: {self.surname}",
                                     f"Age: {str(self.age)}",
                                     f"Gender: {self.gender}", f"Position: {self.position}",
                                     f"Specialization: {self.specialization}"]

                    for data in data_to_write:
                        f.write(data + "\n")

                    print("Folder: '" + person_dir + "' and file 'person_details.txt' created!")
                    f.close()

                else:
                    print("Folder exist! Do you want to overwrite it? [Y or N]")
                    print("If you select 'N' a folder with a suffix of '_' will be created")
                    folder_option = input_str('Y', 'N')

            # --------------------------------------------------
            # spaces and tabulators


            if folder_option == 'Y':
                # Remove all files in path:
                file_list = os.listdir(person_dir_path)
                for element in file_list:
                    os.remove(person_dir_path + "/" + element)
                # Delete existing folder after cleaning it:
                os.rmdir(person_dir_path)
                # Create new folder with person details:
                # Create folder and file.txt:
                os.makedirs(person_dir_path)
                file_path = person_dir_path + "/person_details.txt"
                f = open(file_path, "w")
                # Insert person details into file:
                if chosen_person == 1:
                    data_to_write = ["Person: Employee", "Name: " + name_in, "Surname: " + surname_in,
                                     "Age: " + str(age_in),
                                     "Gender: " + gender_in, "Position: " + position_in,
                                     "Specialization: " + spec_in]
                    for data in data_to_write:
                        f.write(data + "\n")

                if chosen_person == 2:
                    data_to_write = ["Person: Student", "Name: " + name_in, "Surname: " + surname_in,
                                     "Age: " + str(age_in),
                                     "Gender: " + gender_in, "Education stage: " + edu_stg_in,
                                     "Favourite subject: " + fav_sub_in, "Passion: " + passion_in]
                    for data in data_to_write:
                        f.write(data + "\n")

                if chosen_person == 3:
                    data_to_write = ["Person: Child", "Name: " + name_in, "Surname: " + surname_in,
                                     "Age: " + str(age_in),
                                     "Gender: " + gender_in, "Education stage: " + edu_stg_in,
                                     "Favourite toy: " + fav_toy_in, "Favourite fable: " + fav_fable_in]
                    for data in data_to_write:
                        f.write(data + "\n")

                print("Folder: '" + person_dir + "' and file 'person_details.txt' created!")
                f.close()
                exit()

            if folder_option == 'N':
                # Create folder with suffix '_' and file.txt:
                look_path = os.path.dirname(person_dir_path)
                list_files = os.listdir(look_path)

                for act_dir in list_files:
                    if act_dir == person_dir:
                        person_dir_path = look_path + "/" + act_dir + '_'

                os.makedirs(person_dir_path)
                file_path = person_dir_path + "/person_details.txt"
                f = open(file_path, "w")
                # Insert person details into file:
                if chosen_person == 1:
                    data_to_write = ["Person: Employee", "Name: " + name_in, "Surname: " + surname_in,
                                     "Age: " + str(age_in),
                                     "Gender: " + gender_in, "Position: " + position_in,
                                     "Specialization: " + spec_in]
                    for data in data_to_write:
                        f.write(data + "\n")

                if chosen_person == 2:
                    data_to_write = ["Person: Student", "Name: " + name_in, "Surname: " + surname_in,
                                     "Age: " + str(age_in),
                                     "Gender: " + gender_in, "Education stage: " + edu_stg_in,
                                     "Favourite subject: " + fav_sub_in, "Passion: " + passion_in]
                    for data in data_to_write:
                        f.write(data + "\n")

                if chosen_person == 3:
                    data_to_write = ["Person: Child", "Name: " + name_in, "Surname: " + surname_in,
                                     "Age: " + str(age_in),
                                     "Gender: " + gender_in, "Education stage: " + edu_stg_in,
                                     "Favourite toy: " + fav_toy_in, "Favourite fable: " + fav_fable_in]
                    for data in data_to_write:
                        f.write(data + "\n")

                print("Folder: '" + os.path.basename(
                    person_dir_path) + "' and file 'person_details.txt' created!")
                f.close()
                exit()

    except FileNotFoundError:
    print("File not found, please try again")

else:
exit()


class Student(Person):
    def __init__(self):
        super().__init__()
        self.education_stage = "education stage"
        self.favourite_subject = "favourite subject"
        self.passion = "passion"

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
        self.favourite_toy = "favourite toy"
        self.favourite_fable = "favourite fable"

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
