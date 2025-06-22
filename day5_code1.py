x = 10

def change():
    x = 5  # local, doesn't affect outer x
    print("Inside:", x)

change()
print("Outside:", x)  # still 10
