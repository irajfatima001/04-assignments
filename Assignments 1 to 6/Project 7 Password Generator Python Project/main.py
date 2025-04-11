# # password generator

import random
import string

def generate_password(length=12):
  characters =  string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for _ in range(length))
  return password


length = int(input("Enter password length: "))
count = int(input("Enter password count: "))

for i in range(count):
  print(generate_password(length))