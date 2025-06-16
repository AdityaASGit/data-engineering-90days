# Set how many Fibonacci numbers we want (manually, no input())
n= int(input("How many Fibonacci terms do you want?"))

# Start with first two terms
a = 0
b = 1
count = 0

while count < n:
    # Instead of print(a, end=' '), use a basic print
    print(a)

    # Calculate next term without tuple unpacking
    temp = a
    a = b
    b = temp + b

    count = count + 1
