age = int(input("Enter Your Age : "))
price = 12 if age >= 18 else 8
Day = "Monday"

if Day == "Monday":
  price -= 2

print("Movie tickets are priced based on age: $",price)