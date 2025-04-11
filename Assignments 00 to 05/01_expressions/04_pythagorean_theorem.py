import math

def main():
  while True:
    try:
      ab:float = float(input("Enter the length of side AB: "))
      ac:float = float(input("Enter the length of side AC: "))

      if ab <= 0 or ac <= 0 :
        print("Length must be positive number! Try again.\n")
        continue
      # Calculate hypotenuse using Pythagorean theorem
      bc = math.sqrt(ab**2 + ac**2)

      # Display result
      print(f"The length of BC (the hypotenuse) is: {bc:.2f}\n")
      break  # Exit loop after successful calculation

    except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")
if __name__ == '__main__':
  main()
