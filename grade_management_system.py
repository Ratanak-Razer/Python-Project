import csv

# File to store student records
FILE_NAME = "grades.csv"

# Function to initialize CSV file
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Subject", "Marks"])
    except FileExistsError:
        pass  # File already exists

# Function to add a student's grade
def add_grade():
    name = input("Enter student name: ")
    subject = input("Enter subject: ")
    marks = input("Enter marks (out of 100): ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, subject, marks])

    print("✅ Grade added successfully!\n")

# Function to display all grades
def display_grades():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            data = list(reader)
            
            if len(data) == 1:
                print("No records found!")
                return
            
            print("\nStudent Grades:")
            print("=" * 40)
            for row in data:
                print(f"{row[0]} | {row[1]} | {row[2]}")
            print("=" * 40)
    except FileNotFoundError:
        print("No records found. Add grades first!")

# Function to update a student's marks
def update_grade():
    name = input("Enter student name: ")
    subject = input("Enter subject: ")
    
    rows = []
    updated = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[0] == name and row[1] == subject:
                new_marks = input("Enter new marks: ")
                row[2] = new_marks
                updated = True
                break

        if updated:
            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("✅ Marks updated successfully!\n")
        else:
            print("❌ Student record not found!\n")
    except FileNotFoundError:
        print("No records found. Add grades first!")

# Function to calculate the average and assign grades
def calculate_grades():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            
            students = {}
            for row in reader:
                name, subject, marks = row
                marks = int(marks)

                if name in students:
                    students[name].append(marks)
                else:
                    students[name] = [marks]

            print("\nStudent Final Grades:")
            print("=" * 40)
            for name, marks in students.items():
                avg = sum(marks) / len(marks)
                if avg >= 90:
                    grade = "A"
                elif avg >= 80:
                    grade = "B"
                elif avg >= 70:
                    grade = "C"
                elif avg >= 60:
                    grade = "D"
                else:
                    grade = "F"

                print(f"{name} | Average: {avg:.2f} | Grade: {grade}")
            print("=" * 40)
    except FileNotFoundError:
        print("No records found. Add grades first!")

# Main menu
def main():
    initialize_file()

    while True:
        print("\n📚 Grade Management System")
        print("1️⃣ Add Student Grade")
        print("2️⃣ Display All Grades")
        print("3️⃣ Update Student Marks")
        print("4️⃣ Calculate Final Grades")
        print("5️⃣ Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_grade()
        elif choice == "2":
            display_grades()
        elif choice == "3":
            update_grade()
        elif choice == "4":
            calculate_grades()
        elif choice == "5":
            print("📌 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again!")

# Run the program
if __name__ == "__main__":
    main()
