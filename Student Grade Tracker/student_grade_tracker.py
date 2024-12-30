import os

def save_grades_to_file(filename, grades):
    try:
        with open(filename, 'w') as file:
            for subject, grade in grades.items():
                file.write(f"{subject}:{grade}\n")
    except IOError:
        print("Error: Could not save grades to file.")

def load_grades_from_file(filename):
    grades = {}
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    subject, grade = line.strip().split(':')
                    grades[subject] = float(grade)
        except (IOError, ValueError):
            print("Error: Could not read grades from file or file contains invalid data.")
    return grades

def calculate_average(grades):
    if grades:
        return sum(grades.values()) / len(grades)
    return 0.0

def main():
    filename = "grades.txt"
    grades = load_grades_from_file(filename)

    while True:
        print("\nGrade Tracker Menu:")
        print("1. Add/Edit a grade")
        print("2. View all grades")
        print("3. Calculate average grade")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                subject = input("Enter subject name: ").strip()
                try:
                    grade = float(input(f"Enter grade for {subject}: "))
                    if 0 <= grade <= 100:
                        grades[subject] = grade
                        save_grades_to_file(filename, grades)
                        print(f"Grade for {subject} saved successfully.")
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid grade. Please enter a number.")

            elif choice == 2:
                if grades:
                    print("\nGrades:")
                    for subject, grade in grades.items():
                        print(f"{subject}: {grade}")
                else:
                    print("No grades available.")

            elif choice == 3:
                average = calculate_average(grades)
                print(f"\nAverage Grade: {average:.2f}")

            elif choice == 4:
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please select an option from 1 to 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
