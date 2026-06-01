'''Student Data Manager
Description : Store data for 5 students using dictionaries, print topper, class average, and assign grades.'''


# Function to assign grades
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

students = {}

# Input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    
    students[name] = {
        "marks": marks,
        "grade": get_grade(marks)
    }

# Find topper
topper = max(students, key=lambda x: students[x]["marks"])

# Calculate class average
total = sum(student["marks"] for student in students.values())
average = total / len(students)

# Display results
print("\nStudent Details:")
for name, data in students.items():
    print(name, "-> Marks:", data["marks"], ", Grade:", data["grade"])

print("\nTopper:", topper, "-", students[topper]["marks"])
print("Class Average:", average)