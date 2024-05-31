Marks = int(input("Enter your Marks : "))

if Marks >= 101 :
  print("Please veryfi your Marks")
  exit()

if Marks > 90:
  print("A Grade")
elif Marks > 80:
  print("B Grade")
elif Marks > 70:
  print("C Grade")
elif Marks > 60:
  print("D Grade")
elif Marks > 50:
  print("E Grade")
elif Marks > 40:
  print("F Grade")
else:
  print("Next Time Try")
