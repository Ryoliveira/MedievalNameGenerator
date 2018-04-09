"""
This program is a simple Medieval name generator.
User chooses Male or Female with the option to add a surname.
Program runs until user ends session.
"""
from random import randint
import sqlite3

def male(sur, cur):
    """Prints Make name with optional Surname"""
    cur.execute("SELECT count(id) FROM Male_names")
    max_id = cur.fetchone()[0]
    cur.execute("SELECT Male From Male_names WHERE id = ?", (randint(0, max_id),))
    name = cur.fetchone()[0]
    if sur == 'Y':
        name += ' ' + surname(cur)
    print(name)


def female(sur, cur):
    """Prints Female name with optional Surname"""
    cur.execute("SELECT count(id) FROM Female_names")
    max_id = cur.fetchone()[0]
    cur.execute("SELECT Female From Female_names WHERE id = ?", (randint(0, max_id),))
    name = cur.fetchone()[0]
    if sur == 'Y':
        name += ' ' + surname(cur)
    print(name)


def surname(cur):
    """Returns Surname"""
    cur.execute("SELECT count(id) FROM Male_names")
    max_id = cur.fetchone()[0]
    cur.execute("SELECT Surname From Surnames WHERE id = ?", (randint(0, max_id),))
    return cur.fetchone()[0]


if __name__ == '__main__':
    conn = sqlite3.connect("Names.DB")
    cur = conn.cursor()
    loop = True
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
                        male(sur, cur)
                    if gender == "F":
                        female(sur, cur)
            else:
                raise TypeError
            gen_again = input('\nGenerate more names? (Y to continue): ').upper()
            if gen_again != 'Y':
                loop = False
        except (TypeError, ValueError):
            print("Invalid Input")
    print("Good-Bye!")
    conn.close()
