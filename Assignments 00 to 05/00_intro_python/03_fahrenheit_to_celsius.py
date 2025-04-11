def main():
  #input of user for temperture
  degrees_fahrenheit = float(input("Enter the degree in farenhite: "))
  #calculate temp
  degrees_celsius = (degrees_fahrenheit - 32) * 5/9

  print("Temperature:", degrees_fahrenheit, "F =", degrees_celsius, "C")

if __name__ == "__main__":
  main()