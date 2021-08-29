import math

def inp():
    l = int(input("Enter length:"))
    b = int(input("Enter breadth:"))
    h = int(input("Enter height:"))
    return l,b,h

def char_dim(l,b,h):
    k = l**2 + b**2 + h**2
    return k

def volume(b,h,k):
    v = ((b**2)*(h**2))/math.sqrt(k)
    return v

def display(v):
    print("Volume of tromboid is'%.3f'"%v)

def main():
    l,b,h =inp()
    k = char_dim(l,b,h)
    v = volume(b,h,k)
    display(v) 
          
main()
