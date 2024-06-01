n = int(input("Enter Number : "))

sum_of_value = 0

for i in range(1,n+1):
  if i%2 == 0 :
    sum_of_value += 1
print("Sum value is a : " , sum_of_value)