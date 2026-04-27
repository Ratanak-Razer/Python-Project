import csv
import os
import datetime

FILE_NAME = "grades.csv"

# Function to log actions into a file
def log_action(action):
    with open("history.log", "a",encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {action}\n")

# Initialize CSV file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Subject", "Marks", "Grade"])

# Function to add student grades
def add_grades():
    student_id = input("🆔  Enter Student ID: ")
    name = input("🅰️   Enter Name: ")
    subject = input("📑  Enter Subject: ")
    marks = int(input("💯  Enter Marks: "))  # Convert marks to integer

    # Determine grade based on marks
    if 0 <= marks <= 49:
        grade = "F"
    elif 50 <= marks <= 59:
        grade = "E"
    elif 60 <= marks <= 69:
        grade = "D"
    elif 70 <= marks <= 79:
        grade = "C"
    elif 80 <= marks <= 89:
        grade = "B"
    elif 90 <= marks <= 100:
        grade = "A"
    else:
        print("\n❌ Invalid marks input. Please try to input the marks again from 0-100!")
        return  # Exit the function if marks are invalid

    # Append the data to the CSV file
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, subject, marks, grade])
    log_action(f"Added grades for Student ID: {student_id}")
    print("\n✅ Grade added successfully!\n")

# Function to compute the GPA
def compute_gpa():
    student_id = input("Enter Student ID to compute GPA: ")
    total_marks = 0
    subject_count = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[0] == student_id:
                    total_marks += int(row[3])  # Marks are in the 4th column
                    subject_count += 1
            
        if subject_count == 0:
            print("❌ No records found for this student.")
            return
        
        gpa = (total_marks / subject_count) / 20  # Assuming GPA is out of 5
        print(f"\n📊 GPA for Student {student_id}: {gpa:.2f}\n")
        log_action(f"Computed GPA for Student ID: {student_id}")
    
    except FileNotFoundError:
        print("❌ No records found. Please add student grades first.")

# Function to view grades report
def view_grades():
    student_id = input("Enter Student ID to view grades: ")
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip Header
            print("\n📃 Grade Report")
            print("=" * 25)
            for row in reader:
                if row[0] == student_id:
                    print(f"Name: {row[1]} |Subject: {row[2]} | Marks: {row[3]} | Grade: {row[4]}")
                    found = True
            
            if not found:
                print("❌ No records found for this student.")

        log_action(f"Viewed grades for Student ID: {student_id}")
    
    except FileNotFoundError:
        print("❌ No records found. Please add student grades first.")

