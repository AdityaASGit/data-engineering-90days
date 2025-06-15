marks  = int(input("Enter your marks (0-100): "))

if marks > 100 or marks < 0:
    print("Invalid marks please try with correct number")


else:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else: print("Failed")      


