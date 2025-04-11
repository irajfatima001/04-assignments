### Milestone #1: Mars Weight Only
def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = round(earth_weight * 0.378, 2)
    print(f"The equivalent on Mars: {mars_weight}")

if __name__ == "__main__":
    main()


### Milestone #2: All Planets

def main():
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet in gravity_factors:
        planet_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Unknown planet!")

if __name__ == "__main__":
    main()



