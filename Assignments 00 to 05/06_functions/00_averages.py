# Function to calculate average of two numbers
def find_average(num1, num2):
    return (num1 + num2) / 2

def main():
    print("Let's calculate the average of two numbers!")

    # User  inputs
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Average calculate 
    average = find_average(num1, num2)

    # Result show karna
    print("The average of", num1, "and", num2, "is:", average)

# Boilerplate code to run the main function
if __name__ == '__main__':
    main()
