"""
Name: Joseph Fariello
hw1.py

Problem: This program completes hw1

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length"))
    width = eval(input("Enter the width"))
    area = length * width
    print("Area =", area)

calc_rec_area()


def calc_volume():
    length = eval(input("Enter the length"))
    width = eval(input("Enter the width"))
    height = eval(input("Enter the height"))
    volume = length * width * height
    print("Volume =", volume)

calc_volume()


def shooting_percentage():
    TS = eval(input("Enter the player's total shots"))
    SM = eval(input("Enter how many shots the player made"))
    percentage = (SM / TS) * 100
    print("Shooting percentage:", percentage)

shooting_percentage()


def coffee():
    pounds = eval(input("How many pounds of coffee would you like?"))
    cost = ((10.50 + 0.86) * pounds) + 1.50
    print("Your total is $", cost)

coffee()


def kilometers_to_miles():
    kilometers = eval(input("Enter distance in kilometers"))
    miles = kilometers * 0.62
    print("That is ", miles)

kilometers_to_miles()


if __name__ == '__main__':
    pass
