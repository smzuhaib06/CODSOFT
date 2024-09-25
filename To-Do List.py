def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your list.")

def update_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_num - 1] = new_task
        print(f"Task {task_num} has been updated.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to remove: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"'{removed_task}' has been removed from your list.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Options:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
