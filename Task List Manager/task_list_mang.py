import os

# Function to load tasks from the file
def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty task list.")
    return [task.strip() for task in tasks]

# Function to save tasks to the file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to display the menu
def display_menu():
    print("\nTask List Manager")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

# Function to view tasks
def view_tasks(tasks):
    if tasks:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks found.")

# Function to add a task
def add_task(tasks):
    task = input("\nEnter the task description: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Task number out of range.")

# Main function to run the program
def task_manager():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        display_menu()

        choice = input("\nEnter your choice (1-4): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Task list saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the task manager
if __name__ == '__main__':
    task_manager()
