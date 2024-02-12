
import os

def display_menu():
    print("\n~!@#$%^&* To-Do List App *&^%$#@!~")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("\n!!!!!!End-Of-List App!!!!!!")

def view_todo_list():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("Your to-do list is empty.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("Your to-do list is empty.")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added successfully.")

def mark_completed():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                completed_task = tasks.pop(task_number - 1)
                with open("completed.txt", "a") as completed_file:
                    completed_file.write(completed_task)
                with open("todo.txt", "w") as updated_file:
                    updated_file.writelines(tasks)
                print(f"Task '{completed_task.strip()}' marked as completed.")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to delete: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                with open("todo.txt", "w") as updated_file:
                    updated_file.writelines(tasks)
                print(f"Task '{deleted_task.strip()}' deleted successfully.")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    if not os.path.exists("todo.txt"):
        open("todo.txt", "w").close()
    if not os.path.exists("completed.txt"):
        open("completed.txt", "w").close()
    main()

