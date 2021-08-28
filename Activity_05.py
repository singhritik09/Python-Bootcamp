lst = []

print("Enter 5 elements of list:")
for i in range(0,5):
    elements=int(input())
    lst.append(elements)
    
print(lst)

sum = 0
for i in range(0,len(lst)):
    sum = sum + lst[i]
print("Sum of elements is:",sum)
