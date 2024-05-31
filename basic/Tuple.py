# tea_types = ("Green","Masala","Lemon")
# print(type(tea_types))
# print(tea_types)
# print(tea_types[0])

more_Types = ("Black",("Green","Masala",("Oolong","Chai")))
# print(more_Types[1][2][1])

if "Oolong" in more_Types[1][2][0]:
  print("Yes")
else:
  print("No")