"""
This program is a simple Medieval name generator.
User chooses Male or Female with the option to add a surname.
Program runs until user ends session.
"""
from random import randint

def load_names():
    """Loads all name lists"""
    # Get male names
    with open('male_names.txt', 'r') as file:
        names = file.readlines()
        male_name_list = [name.strip() for name in names if name.strip() != '']
    # Get female names
    with open('female_names.txt', 'r') as file:
        names = file.readlines()
        female_name_list = [name.strip() for name in names if name.strip() != '']
    # Get surnames
    with open('surnames.txt', 'r') as file:
        surnames = file.readlines()
        surname_list = [surname.strip() for surname in surnames if surname.strip() != '']
    return male_name_list, female_name_list, surname_list


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
    male_name_list, female_name_list, surname_list = load_names() # Load name lists
    print("Welcome to the medieval name generator!\n"
          "Please enter a gender\n")
    while loop:
        try:
            gender = input("\"M\" for Male or \"F\" for Female:").title()
            if len(gender) == 1:
                sur = input("Add a surname? Y or N (N by default): ").upper()
                if gender == "M":
                    print("\nYour Male Name:", end=' ')
                    male(sur)
                if gender == "F":
                    print("\nYour Female Name:", end=' ')
                    female(sur)
            else:
                raise TypeError
                print("Enter M or F")
            gen_again = input('\nGenerate another name? (Y to continue): ').upper()
            if gen_again != 'Y':
                loop = False
        except TypeError:
            print("Enter M or F")
    print("Good-Bye!")

