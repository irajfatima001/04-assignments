# Constant value for the speed of light (m/s)
C = 299792458

def main():
  while True:
    try:
      mass_in_kg = float(input("Enter kilos of mass (or type 0 to exit): "))
      if mass_in_kg == 0:
                print("Exiting program...")
                break  # Exit loop if user enters 0

      # Calculate energy (E = m * C^2)
      energy_in_joules = mass_in_kg * (C ** 2)

      # Display results
      print("\ne = m * C^2...\n")
      print(f"m = {mass_in_kg} kg")
      print(f"C = {C} m/s\n")
      print(f"{energy_in_joules:.5e} joules of energy!\n")  # Exponential notation for large numbers

    except ValueError:
      print("❌ Invalid input! Please enter a valid number.")

# Run the main function
if __name__ == '__main__':
    main()