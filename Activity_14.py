n = int(input("Enter an integer:"))

def prime():
    for i in range(2,int(n/2)+1):
        if (n%i==0):
            print(n, "is not a Prime Number")
            break
    else:
        print(n,"is a Prime number")

prime()
