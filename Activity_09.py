import math

l = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
h = int(input("Enter the height:"))

k = l**2 + b**2 + h**2

v = ((h*h) * (b*b))/math.sqrt(k)

radius = ((3/4)*v*3.14*(1/3))

print("Volume of trobolide='%0.3f'"%v)
print("Radius of the circle='%0.3f"%radius)

