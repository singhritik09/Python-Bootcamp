import math

l = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
h = int(input("Enter the height:"))

k = l**2 + b**2 + h**2

v = ((h*h) * (b*b))/math.sqrt(k)

print("Volume of trobolide='%0.3f'"%v)

