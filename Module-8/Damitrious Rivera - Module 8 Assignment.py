# Damitrious Rivera - Module 8 Assignment
import json

# Function to print the student list
def print_students(students):
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']}, Email = {s['Email']}")

# Load JSON file
with open('student.json', 'r') as file:
    students = json.load(file)

print("Original Student List:")
print_students(students)

# Add your own record
new_student = {
    "F_Name": "Damitrious",
    "L_Name": "Rivera",
    "Student_ID": 21458135,
    "Email": "damrivera@my365.bellevue.edu"
}

students.append(new_student)

print("\nUpdated Student List:")
print_students(students)

# Write updated data back to JSON file
with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file was updated successfully!")