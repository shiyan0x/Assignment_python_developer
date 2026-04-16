def show_menu():
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    with open("task.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def view_task():
    try:
        with open("task.txt", "r") as file:
            task_list = file.readlines()
    except FileNotFoundError:
        task_list = []
    
    if not task_list:
        print("No tasks found!")
    else:
        for index, task in enumerate(task_list):
            print(f"{index + 1}. {task}")

def delete_task():
    view_task()
    try:
        with open("task.txt", "r") as file:
            task_list = file.readlines()
    except FileNotFoundError:
        task_list = []
        
    if task_list:
        try:
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(task_list):
                task_list.pop(task_index)
                with open("task.txt", "w") as file:
                    file.writelines(task_list)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid input, please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
