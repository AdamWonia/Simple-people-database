def select_option(lb, ub):
    """ add docstring """
    while True:
        option = input("Insert option: ")
        if option.isnumeric() and int(option) in range(lb, ub+1):
            break
        else:
            print("You put invalid option, insert number between {} and {}".format(lb, ub))

    return int(option)


def basic_person_details():
    """ add docstring """
    print("Insert name: ")
    name_in = input_str().strip()
    print("Insert surname: ")
    surname_in = input_str().strip()
    print("Insert age: ")
    age_in = input_int()
    print("Insert gender [M or F]: ")
    gender_in = input_str('M', 'F').strip()

    return [name_in, surname_in, age_in, gender_in]


def input_int():
    """ add docstring """
    while True:
        try:
            input_data = int(input())
            break
        except:
            print("You put invalid data, please enter an integer")

    return input_data


def input_str(option1=None, option2=None):
    """ add docstring """
    while True:
        input_data = input()
        if option1 is None and option2 is None:
            if ''.join(input_data.split()).isalpha():
                break
            else:
                print("You put invalid data, please try again")

        if option1 is not None or option2 is not None:
            input_data = input_data.upper().strip()
            if input_data.isalpha() and (input_data == option1 or input_data == option2):
                break
            else:
                print("You put invalid data, please try again")

    return input_data
