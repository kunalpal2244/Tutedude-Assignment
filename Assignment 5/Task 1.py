STUDENT_MARKS = {"kunal":85 , "Arav":24 , "Kukku":89 , "piyush": 78}
name =input("Enter the student name :")
if name in STUDENT_MARKS:
    print(f"{name}'s marks:{STUDENT_MARKS[name]}")
else:
    print("Student not found in the records")
