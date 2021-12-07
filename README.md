# Employee management with Flask framework

## Description

This repository contains my first project made in Python. Simple people database is a program that allows you to add people to a folder selected by the user.

The user can select 3 types of people: 
* Employee,
* Student,
* Child.

Every person has certain information to fill in. There is basic information such as name, age and gender, but also additional information for each type of person.

After entering the data, the user has the opportunity to save the person to a selected folder, in which the file **person_details.txt** is created, containing data entered by the user.

Apart from the option of adding a new person, there is a possibility to rename or delete existing folder.

## Creating a virtual environment

Open a terminal in your project directory and type the following command:

```bash
python -m venv venv
```
This will create a virtual environment named **venv**. To activate the virtual environment type the following command in your terminal:

```bash
"venv/scripts/activate.bat"
```

## Launch

To run the application, use the **main.py** file found in the repository. You can use a terminal by typing the following command or run it from the IDE.

```bash
python main.py
```

When you start the program you will see the menu shown below:

```python
What would like to do?
1 - Add new person
2 - Rename existing person
3 - Remove person
Insert option: 
```
You should now choose what you want to do next. Once you have selected option 1, you will be asked to select the person to add. You have three options to choose from.

```python
Select the person you want to add to the base:
1 - Employee
2 - Student
3 - Child
Insert option: 
```
The next step is to fill in information about the selected person. You will then be asked if you want to save this person's data to a file. If you select yes, you will need to choose a folder where the data will be saved.

You can also rename an existing folder or delete it from the database.

## Closing words

File **person_classes.py** contains classes of people with appropriate fields and methods. File **control_input.py** contains a function to retrieve the relevant data from the terminal.

The program can be further developed, for example, by adding more types of people, additional information, the possibility of editing information about an existing person, adding persons to the internet database, etc.

The author assumes no responsibility for accidental deletion or renaming of an important folder to the user. Please be careful when using this program.

I hope you enjoy using it.
