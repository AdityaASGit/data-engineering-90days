try:

    marks  = int(input("Enter your marks (0-100): "))

    if marks > 100 or marks < 0:
        raise ValueError("Invalid marks,must be between 0-100.")
except ValueError as ve:
    print("input Error:", ve)

except Exception as e:
    print("Something went wrong:", e)


else:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else: 
        print("Failed")      

finally:
    print("Program Finished, Thank you!")
