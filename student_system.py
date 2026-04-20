# ============================================================
# Student Data Management System
# A simple console app to manage student records using Python
# ============================================================

import json
import os

# ---------- File name to save/load data ----------
DATA_FILE = "students.json"


# ---------- 1. Load data from file ----------
def load_students():
    """Load student records from a JSON file when the program starts."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []  # Return empty list if file doesn't exist yet


# ---------- 2. Save data to file ----------
def save_students(students):
    """Save all student records to a JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


# ---------- 3. Add a new student ----------
def add_student(students):
    """Prompt the user for details and add a new student to the list."""
    print("\n--- Add New Student ---")

    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    roll = input("Enter roll number: ").strip()
    if not roll:
        print("Error: Roll number cannot be empty.")
        return

    # Check if roll number already exists
    for student in students:
        if student["roll"] == roll:
            print(f"Error: Roll number '{roll}' already exists.")
            return

    # Validate marks input
    try:
        marks = float(input("Enter marks (0-100): "))
        if not (0 <= marks <= 100):
            print("Error: Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Please enter a valid number for marks.")
        return

    # Create a student record as a dictionary
    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print(f"Student '{name}' added successfully!")


# ---------- 4. View all students ----------
def view_students(students):
    """Display all student records in a formatted table."""
    print("\n--- All Students ---")

    if not students:
        print("No student records found.")
        return

    # Print table header
    print(f"{'No.':<5} {'Name':<20} {'Roll No.':<15} {'Marks':<10}")
    print("-" * 50)

    # Print each student's details
    for i, student in enumerate(students, start=1):
        print(f"{i:<5} {student['name']:<20} {student['roll']:<15} {student['marks']:<10}")


# ---------- 5. Search student by roll number ----------
def search_student(students):
    """Search for a student using their roll number."""
    print("\n--- Search Student ---")

    roll = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll"] == roll:
            print(f"\nStudent Found:")
            print(f"  Name    : {student['name']}")
            print(f"  Roll No.: {student['roll']}")
            print(f"  Marks   : {student['marks']}")
            return

    print(f"No student found with roll number '{roll}'.")


# ---------- 6. Update student details ----------
def update_student(students):
    """Find a student by roll number and update their details."""
    print("\n--- Update Student ---")

    roll = input("Enter roll number of student to update: ").strip()

    for student in students:
        if student["roll"] == roll:
            print(f"Found: {student['name']} | Marks: {student['marks']}")
            print("Press Enter to keep the current value.")

            # Update name
            new_name = input(f"New name [{student['name']}]: ").strip()
            if new_name:
                student["name"] = new_name

            # Update marks
            new_marks_input = input(f"New marks [{student['marks']}]: ").strip()
            if new_marks_input:
                try:
                    new_marks = float(new_marks_input)
                    if 0 <= new_marks <= 100:
                        student["marks"] = new_marks
                    else:
                        print("Invalid marks. Keeping old value.")
                except ValueError:
                    print("Invalid input. Keeping old marks.")

            save_students(students)
            print("Student updated successfully!")
            return

    print(f"No student found with roll number '{roll}'.")


# ---------- 7. Delete a student ----------
def delete_student(students):
    """Remove a student record by roll number."""
    print("\n--- Delete Student ---")

    roll = input("Enter roll number of student to delete: ").strip()

    for i, student in enumerate(students):
        if student["roll"] == roll:
            confirm = input(f"Are you sure you want to delete '{student['name']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                students.pop(i)
                save_students(students)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print(f"No student found with roll number '{roll}'.")


# ---------- 8. Display menu ----------
def show_menu():
    """Print the main menu options."""
    print("\n=============================")
    print("  Student Data Management System")
    print("=============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("-----------------------------")


# ---------- 9. Main program ----------
def main():
    """Main function — loads data and runs the menu loop."""
    students = load_students()  # Load existing data at startup
    print("Welcome to the Student Data Management System!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Goodbye! Data has been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# ---------- Entry point ----------
if __name__ == "__main__":
    main()