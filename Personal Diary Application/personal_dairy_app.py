import os
from datetime import datetime

def write_entry():
    print("\nEnter your diary entry below. Type 'END' on a new line to save and exit.\n")
    entries = []
    while True:
        entry = input()
        if entry.strip().upper() == 'END':
            break
        entries.append(entry)
    
    # Add timestamp to the entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as file:
        file.write(f"\nEntry on {timestamp}:\n")
        file.write("\n".join(entries))
        file.write("\n---\n")  # Separator between entries
    print("Your entry has been saved!")

def view_entries():
    try:
        with open("diary.txt", "r") as file:
            print("\nYour Diary Entries:")
            print(file.read())
    except FileNotFoundError:
        print("Diary file not found. Please write an entry first.")
    except PermissionError:
        print("Permission denied. Unable to access the diary file.")

def main():
    while True:
        print("\nPersonal Diary Application")
        print("1. Write a new entry")
        print("2. View previous entries")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
