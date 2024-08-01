import json
import os

TODO_FILE = "todo.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks in your to-do list.")
    else:
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")

def add_todo(todos):
    task = input("Enter a new task: ")
    todos.append(task)
    print(f"Task added: {task}")

def remove_todo(todos):
    list_todos(todos)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(todos):
            removed_task = todos.pop(index)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todos = load_todos()

    while True:
        print("\nTo-Do Application")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_todo(todos)
        elif choice == '3':
            remove_todo(todos)
        elif choice == '4':
            save_todos(todos)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
