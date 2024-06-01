numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

number_count_positive = 0
number_count_negative = 0

for num in numbers:
  if num > 0:
    number_count_positive += 1
print("Poitive Numbers is a : " , number_count_positive)


# Negative Numbers 

for num in numbers:
  if num < 0 :
    number_count_negative -= 1
print("Negative Numbers is a : " , number_count_negative)