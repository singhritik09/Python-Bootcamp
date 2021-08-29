n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))

greatest = 0

if n1>n2 and n1>n3:
    greatest = n1
elif n2>n1 and n2>n3:
    greatest =n2
else:
    greatest=n3
    
print(greatest ,"is greatest number among",n1,n2,n3)
