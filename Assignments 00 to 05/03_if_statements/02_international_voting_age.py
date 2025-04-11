# Voting ages for fictional countries
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    # Get user's age
    user_age = int(input("How old are you? "))

    # Check eligibility for each country
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")

    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")

    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

# Call main function
if __name__ == '__main__':
    main()
