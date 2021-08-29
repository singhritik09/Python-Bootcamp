n1 = int(input("Enter the starting number:"))
n2 = int(input('Enter the end number:'))

for i in range(n1,n2):
    if i%2==0:
        continue
    print(i)
