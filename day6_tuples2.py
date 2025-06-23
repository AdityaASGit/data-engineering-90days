def analyze_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    return (total, average, highest, lowest)  # returning a tuple

marks = [88, 76, 92, 85, 69]

result = analyze_scores(marks)

print(f"Total: {result[0]}")
print(f"Average: {result[1]:.2f}")
print(f"Highest: {result[2]}")
print(f"Lowest: {result[3]}")