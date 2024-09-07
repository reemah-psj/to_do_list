todo_list = []
def show_menu():
    print("\nTo-Do List Options:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")
def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
def remove_task():
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")
while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the to-do list. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
