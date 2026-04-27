import os 
from colorama import Fore, Style
from module import add_grades,initialize_file,compute_gpa,view_grades,log_action
os.system('cls')
def main():
    initialize_file()
    
    while True:
        print(Fore.YELLOW,"📚 Grade Management System", Style.RESET_ALL)
        print("1️⃣  Add Student Grades")
        print("2️⃣  Compute GPA")
        print("3️⃣  View Grade Report")
        print("4️⃣  Exit")

        choice = input("->. Enter your choice (1-4): ")
        if choice == "1":
            os.system('cls')
            log_action("🅰️ Add Student Grades")
            add_grades()
        elif choice == "2":
            os.system('cls')
            log_action("🧮 Compute GPA")
            compute_gpa()
        elif choice == "3":
            os.system('cls')
            log_action("📃 View Grade Report")
            view_grades()
        elif choice == "4":
            os.system('cls')
            log_action("👋 Exit Program")
            print("\n📌 Exiting program. Goodbye!")
            return
        else:
            os.system('cls')
            log_action("❌ Invalid Data Input!")
            print("❌ Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
    