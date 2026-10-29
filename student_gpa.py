# Name: NQuisenberry
# File: student_gpa.py
# Description: Accept student names and GPAs, then report Dean's List and Honor Roll eligibility.

while True:
    last_name = input("Enter the student's last name (or ZZZ to quit): ")
    if last_name == "ZZZ":
        break

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    student_name = f"{first_name} {last_name}"
    if gpa >= 3.5:
        print(f"{student_name} has made the Dean's List.")
    if gpa >= 3.25:
        print(f"{student_name} has made the Honor Roll.")
