print("number calculator")
number_1 = input("enter a number (don't use more than 2 characters)\n")[:2]
number_2 = input("enter another number (don't use more than 2 characters)\n")[:2]
try:
  number_1 = eval(number_1)
  number_2 = eval(number_2)
  print(number_1 + number_2)
  print(number_1 - number_2)
  print(number_1 * number_2)
  print(number_1 / number_2)
  try:
    print(max(number_1, number_2))
    print(min(number_1, number_2))
  except:
    print('PlaygroundsCTF{REDACTED}')
except:
  print("no")