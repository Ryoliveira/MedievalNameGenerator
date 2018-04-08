"""
This program is a simple Medieval name generator.
User chooses Male or Female with the option to add a surname.
Program runs until user ends session.
"""
from random import randint


def load_names():
    """Loads all name lists"""
    with open('male_names.txt', 'r') as file:  # Get male names
        male_name_list = [name.strip() for name in file.readlines() if name.strip() != '']
    with open('female_names.txt', 'r') as file:  # Get female names
        female_name_list = [name.strip() for name in file.readlines() if name.strip() != '']
    with open('surnames.txt', 'r') as file:  # Get surnames
        surname_list = [surname.strip() for surname in file.readlines() if surname.strip() != '']
    return male_name_list, female_name_list, surname_list  # Return all three lists


def male(sur):
    """Prints Make name with optional Surname"""
    name = male_name_list[randint(0, len(male_name_list))]
    if sur == 'Y':
        name += ' ' + surname()
    print(name)


def female(sur):
    """Prints Female name with optional Surname"""
    name = female_name_list[randint(0, len(female_name_list))]
    if sur == 'Y':
        name += ' ' + surname()
    print(name)


def surname():
    """Returns Surname"""
    return surname_list[randint(0, len(surname_list))]


if __name__ == '__main__':
    loop = True
    male_name_list, female_name_list, surname_list = load_names()  # Load name lists
    print("Welcome to the Medieval Name Generator!\n")
    while loop:
        try:
            num_names = int(input("How many names would you like to generate?\n"))
            gender = input("\"M\" for Male or \"F\" for Female:").upper()
            if len(gender) == 1 and gender == "M" or gender == 'F' and num_names > 0:
                sur = input("Add a surname? Y or N (N by default): ").upper()
                for i in range(num_names):
                    print(str(i + 1) + ".", end='  ')
                    if gender == "M":
                        male(sur)
                    if gender == "F":
                        female(sur)
            else:
                raise TypeError
            gen_again = input('\nGenerate more names? (Y to continue): ').upper()
            if gen_again != 'Y':
                loop = False
        except (TypeError, ValueError):
            print("Invalid Input")
    print("Good-Bye!")
