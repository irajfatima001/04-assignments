def main():
  lst = []
  while True:
    val = input("Enter a value: ")

    if val == "":
      break
    lst.append(val)
  print("Here's the list:", lst)
if __name__ == "__main__" :
  main()
