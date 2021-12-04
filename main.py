from classes import *
from functions import *
from tkinter import Tk, filedialog as fd
import time
import os

# Create widget of Tk:
root = Tk()
root.withdraw()
root.attributes('-topmost', True)

if __name__ == "__main__":
    print("What would like to do?")
    print("1 - Add new person")
    print("2 - Rename existing person")
    print("3 - Remove person")

    # Choosing the start option:
    start_option = select_option(1, 3)

    if start_option == 1:
        print("Chosen option: {} - {}".format(start_option, "Add new person"))
        print("Select the person you want to add to the base:")
        print("1 - Employee")
        print("2 - Student")
        print("3 - Child")

        # Choosing the person to add:
        chosen_person = select_option(1, 3)
        basic_info = []

        # Chosen person:
        if chosen_person == 1:
            print("Chosen option: {} - {}".format(chosen_person, "Employee"))
            # Creating employee:
            employee = Employee()
            # Insert Employee information:
            employee.get_employee_details()
            # Show entered data:
            employee.show_employee_details()

        if chosen_person == 2:
            print("Chosen option: {} - {}".format(chosen_person, "Student"))
            # Creating student:
            student = Student()
            # Insert student information:
            student.get_student_detail()
            # Show entered data:
            student.show_student_details()

        if chosen_person == 3:
            print("Chosen option: {} - {}".format(chosen_person, "Child"))
            # Creating child:
            child = Child()
            # Insert person information:
            child.get_child_details()
            # Show entered data:
            child.show_child_details()





        # Saving person details to file:
        print("Do you want to save the person's data to a file? [Y or N]")
        save_option = input_str('Y', 'N')

        if save_option == 'Y':
            print("Choose a directory to save: ")
            print("Note: A folder and file will be created with the person data")
            time.sleep(2)

            # Extract basic person data to the relevant variables:
            name_in = basic_info[0]
            surname_in = basic_info[1]
            age_in = basic_info[2]
            gender_in = basic_info[3]

            # Choosing directory:
            try:
                chosen_path = fd.askdirectory()
                if chosen_path == '':
                    raise FileNotFoundError

                print("Chosen path: " + chosen_path + "\n")

                # Create person folder in chosen directory:
                person_dir = name_in + " " + surname_in
                person_dir_path = chosen_path + "/" + person_dir
                if not os.path.isdir(person_dir_path):
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
                                         "Age: " + str(age_in), "Gender: " + gender_in,
                                         "Favourite toy: " + fav_toy_in, "Favourite fable: " + fav_fable_in]
                        for data in data_to_write:
                            f.write(data + "\n")

                    print("Folder: '" + person_dir + "' and file 'person_details.txt' created!")
                    f.close()
                else:
                    print("Folder exist! Do you want to overwrite it? [Y or N]")
                    print("If you select 'N' a folder with a suffix of '_' will be created")
                    folder_option = input_str('Y', 'N')

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

                if save_option == 'N':
                    exit()

            except FileNotFoundError:
                print("File not found, please try again")

    if start_option == 2:
        print("Chosen option: {} - {}".format(start_option, "Rename existing person"))
        print("Select folder to rename:")
        # Select folder to rename:
        time.sleep(2)
        try:
            chosen_path = fd.askdirectory()
            if chosen_path == '':
                raise FileNotFoundError

            print(chosen_path)
            print("Selected folder: " + chosen_path)
            print("Insert new folder name: ")
            new_fold_name = input()
            new_fold_dir = os.path.dirname(chosen_path) + "/" + new_fold_name

            if os.path.isdir(os.path.dirname(chosen_path) + "/" + new_fold_name):
                print("Folder with this name already exists! Please try again")
            else:
                os.rename(chosen_path, new_fold_dir)
                print(
                    "Folder '" + os.path.basename(chosen_path) + "' renamed to: '" + os.path.basename(
                        new_fold_dir) + "'!")
            exit()

        except FileNotFoundError:
            print("File not found, please try again")

    if start_option == 3:
        print("Chosen option: {} - {}".format(start_option, "Remove person"))
        print("Select folder to delete:")
        # Select folder to delete:
        time.sleep(2)
        try:
            chosen_path = fd.askdirectory()
            if chosen_path == '':
                raise FileNotFoundError

            print("Selected folder: " + chosen_path)
            # Remove all files in path:
            file_list = os.listdir(chosen_path)

            for element in file_list:
                os.remove(chosen_path + "/" + element)

            # Delete existing folder after cleaning it:
            os.rmdir(chosen_path)
            print("Folder: '" + os.path.basename(chosen_path) + "' removed!")
            exit()

        except FileNotFoundError:
            print("File not found, please try again")
