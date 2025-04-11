INCHES_IN_FOOT = 12 # there is 12 inches in one foot

def main():
  while True:
    try:
        # Get input from the user
        feet = float(input("Enter number of feet (or type 0 to exit): "))

        if feet == 0:
            print("Exit program...")
            break  # Exit loop if user enters 0

        # Convert feet to inches
        inches = feet * INCHES_IN_FOOT

        # Display result
        print(f"{feet} feet is {inches} inches!\n")

    except ValueError:
       print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
  main()
