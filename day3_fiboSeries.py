number = int(input("How many Fibonacci terms do you want?"))
a, b = 0, 1
count = 0
while count < number:
    print(a, end=' ')
    a, b = b, a + b
    count = count+1
