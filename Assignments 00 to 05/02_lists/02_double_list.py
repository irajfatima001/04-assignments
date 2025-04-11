def double_numbers(numbers: list[int]) -> list[int]:
  return [num * 2 for num in numbers] # List comprehension for efficiency
def main():
  numbers=[1,2,3,4,5]
  doubled_numbers=double_numbers(numbers) # Double each number
  print(doubled_numbers)
if __name__=="__main__":
  main()