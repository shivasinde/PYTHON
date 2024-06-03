number = int(input("Enter a number : "))
factorial = 1

while factorial > 0 :
  factorial = factorial * number
  number = number - 1
print("factorial number is " , factorial)