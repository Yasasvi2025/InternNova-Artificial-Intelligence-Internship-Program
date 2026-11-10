# AI-Based Student Result Prediction

name = input("Enter student name: ")
marks = int(input("Enter student marks: "))

if marks >= 35:
    print(name, "is predicted to PASS")
else:
    print(name, "is predicted to FAIL")