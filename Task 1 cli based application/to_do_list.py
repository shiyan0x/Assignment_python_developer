import os

FILE_NAME = "task.txt"

def show_menu():
    print("\n" + "="*30)
    print("   To-Do List Application")
    print("="*30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("="*30)

def add_task():
    task = input("\nEnter the task: ").strip()
    if task:
        with open(FILE_NAME, "a") as file:
            file.write(task + "\n")
        print(f"-> Task '{task}' added successfully!")
    else:
        print("-> Task cannot be empty!")

def view_task():
    try:
        with open(FILE_NAME, "r") as file:
            task_list = file.readlines()
    except FileNotFoundError:
        task_list = []
    
    if not task_list:
        print("\n-> No tasks found!")
        return False
    else:
        print("\n" + "-"*20)
        print("     Your Tasks")
        print("-"*20)
        for index, task in enumerate(task_list):
            print(f"[{index + 1}] {task.strip()}")
        print("-"*20)
        return True

def delete_task():
    has_tasks = view_task()
    if not has_tasks:
        return
        
    try:
        with open(FILE_NAME, "r") as file:
            task_list = file.readlines()
    except FileNotFoundError:
        task_list = []
        
    if task_list:
        try:
            task_index = int(input("\nEnter the task number to delete: ")) - 1
            if 0 <= task_index < len(task_list):
                deleted_task = task_list.pop(task_index).strip()
                with open(FILE_NAME, "w") as file:
                    file.writelines(task_list)
                print(f"-> Task '{deleted_task}' deleted successfully!")
            else:
                print("-> Invalid task number!")
        except ValueError:
            print("-> Invalid input! Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("\n-> Exiting the application. Goodbye!\n")
            break
        else:
            print("-> Invalid choice! Please select from 1 to 4.")

if __name__ == "__main__":
    main()
