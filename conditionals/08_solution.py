password = input("Enter Your Password : ")

if len(password) < 6:
  strength = "weak"
elif len(password) <= 10 : 
  strength = "medium"
else:
  strength = "storng"

  print("password strength : " , strength)
