def main():
  dividend = int(input("Enter the dividend: "))
  divisor = int(input("Enter the divisor: "))

  if divisor == 0:
    print("Error: Division by zero is not allowed.")
    return
  quotient = dividend / divisor

  remainder = dividend % divisor

  # Display the result using f-string
  print(f"The result of this division is {quotient} with a remainder of {remainder}.")

if __name__ == "__main__":
  main()