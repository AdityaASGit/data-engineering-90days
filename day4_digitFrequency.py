num = int(input("Enter a number: "))
frequency = {}  # This will store digit counts

while num > 0:
    digit = num % 10  # Get last digit

    # Check if the digit is already in the dictionary
    if digit in frequency:
        frequency[digit] = frequency[digit] + 1  # Increment count
    else:
        frequency[digit] = 1  # First time seeing this digit

    num = num // 10  # Remove last digit

# Display digit frequencies
print("Digit frequencies:")
for digit in sorted(frequency):
    print(str(digit) + ":", frequency[digit])
