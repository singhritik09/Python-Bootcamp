n = int(input("Enter an integer:"))

def prime():
    if n==1 or n==2:
        print("Given integer is prime")
    
    for i in range(2,n):
        if n%i==0:
            print("Given integer is not a prime number")
            break
        else:
            print("Given integer is a prime number")
            break
prime()
