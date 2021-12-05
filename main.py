from person_classes import *
from control_input import *
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

        # Chosen person:
        if chosen_person == 1:
            print("Chosen option: {} - {}".format(chosen_person, "Employee"))
            # Creating employee:
            employee = Employee()
            # Insert Employee information:
            employee.get_employee_details()
            # Show entered data:
            employee.show_employee_details()
            # Saving Employee details to file:
            print("Do you want to save the person's data to a file? [Y or N]")
            save_option = input_str('Y', 'N')
            employee.save_employee_to_file(save_option)

        if chosen_person == 2:
            print("Chosen option: {} - {}".format(chosen_person, "Student"))
            # Creating employee:
            student = Student()
            # Insert Employee information:
            student.get_student_detail()
            # Show entered data:
            student.show_student_details()
            # Saving Employee details to file:
            print("Do you want to save the person's data to a file? [Y or N]")
            save_option = input_str('Y', 'N')
            student.save_student_to_file(save_option)

        if chosen_person == 3:
            print("Chosen option: {} - {}".format(chosen_person, "Child"))
            # Creating employee:
            child = Child()
            # Insert Employee information:
            child.get_child_details()
            # Show entered data:
            child.show_child_details()
            # Saving Employee details to file:
            print("Do you want to save the person's data to a file? [Y or N]")
            save_option = input_str('Y', 'N')
            child.save_child_to_file(save_option)

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
            # Insert new folder name:
            new_folder_name = input()
            new_folder_dir = os.path.dirname(chosen_path) + "/" + new_folder_name
            # Check if it already exists:
            if os.path.isdir(os.path.dirname(chosen_path) + "/" + new_folder_name):
                print("Folder with this name already exists! Please try again")
            else:
                os.rename(chosen_path, new_folder_dir)
                print(
                    "Folder '" + os.path.basename(chosen_path) + "' renamed to: '" + os.path.basename(
                        new_folder_dir) + "'!")
            exit()
        # Display a message if the directory is not found:
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
        # Display a message if the directory is not found:
        except FileNotFoundError:
            print("File not found, please try again")
