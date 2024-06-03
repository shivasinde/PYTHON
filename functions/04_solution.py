import math
radius = int(input("Enter your  radius : "))

def circle( radius):
  return math.pi * radius ** 2

res = circle(radius)
print("area of circle of radius : ", res)