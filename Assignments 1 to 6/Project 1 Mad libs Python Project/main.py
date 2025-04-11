#Project-01 (Mad Libs)

import time

def mad_libs():
    print("\n🎭 Welcome to the Hilarious Mad Libs Game! 🎭")
    time.sleep(1)

    print("\n🤪 Fill in the blanks to create your crazy story! 🚀")


    name = input("Enter a funny name: ")
    place = input("Enter a weird place: ")
    animal = input("Enter a strange animal: ")
    food = input("Enter a type of food: ")
    adjective1 = input("Enter a silly adjective: ")
    adjective2 = input("Enter another adjective: ")
    verb1 = input("Enter a crazy action verb: ")
    verb2 = input("Enter another action verb: ")
    sound = input("Enter a funny sound (e.g. BOOM, SPLAT!): ")


    story = f"""
    One day, {name} decided to visit {place}.
    But guess what? As soon as {name} arrived, a {adjective1} {animal} jumped out of nowhere and screamed "{sound}!!"
    {name} got so scared that they immediately started {verb1} all over the place.
    Suddenly, a {adjective2} waiter appeared, holding a giant plate of {food}.
    Instead of running away, the {animal} grabbed the food and started {verb2} like there was no tomorrow!
    {name} just stood there, watching the madness, wondering if they had just entered a parallel universe.
    And from that day on, {name} was known as the "Legend of {place}"! 🤣
    """
