number = int(input("Give a number : "))
is_prime = True

if number > 1:
  for num in range(2 , number):
    if (num % 2 == 0) :
      is_prime = False
print(is_prime)