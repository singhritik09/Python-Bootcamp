def main():
    a, b = input_numbers()
    summation = add(a, b)
    display(a, b, summation)

def input_numbers():
    a = int(input("Enter first Number:"))
    b = int(input("Enter Second Number:"))
    return a,b

def add(a,b):
    return(a+b)

def display(a,b,summation):
    print(f"{a} + {b} = {summation}")
    
main()
