def print_table(n, m):
    for i in range(1, m + 1):
        print(f"{n} x {i} = {n * i}")

n = int(input("Enter a number for the multiplication table: "))
print_table(n, 14)

