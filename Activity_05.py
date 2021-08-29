inp = input("Enter the numbers:")
numbers = inp.split()

lst = list(numbers)
print(lst)
sum =0
for i in numbers:
    sum = sum + int(i)
print('Sum is:',sum)
    
