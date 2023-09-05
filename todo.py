# Initialize the to-do list
tasks = []

# Load tasks from a text file
def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                task_data = line.strip().split(',')
                task = {
                    'description': task_data[0],
                    'priority': task_data[1],
                    'completed': task_data[2] == 'True'
                }
                tasks.append(task)
    except FileNotFoundError:
        tasks = []

# Save tasks to a text file
def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['description']},{task['priority']},{task['completed']}\n")

# Load tasks on program start
load_tasks()

# Menu loop
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View tasks")
    print("4. Mark a task as completed")
    print("5. Organize tasks by priority")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # Add a task
        task_description = input("Enter task description: ")
        priority = input("Enter priority (high, medium, low): ")
        task = {"description": task_description, "priority": priority, "completed": False}
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        # Delete a task
        task_to_delete = input("Enter the task number to delete: ")
        if task_to_delete.isdigit() and int(task_to_delete) >= 1 and int(task_to_delete) <= len(tasks):
            deleted_task = tasks.pop(int(task_to_delete) - 1)
            print(f"Task '{deleted_task['description']}' deleted.")
        else:
            print("Invalid task number.")

    elif choice == '3':
        # View tasks
        if not tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['description']} (Priority: {task['priority']}, Completed: {'Yes' if task['completed'] else 'No'})")

    elif choice == '4':
        # Mark a task as completed
        task_to_complete = input("Enter the task number to mark as completed: ")
        if task_to_complete.isdigit() and int(task_to_complete) >= 1 and int(task_to_complete) <= len(tasks):
            tasks[int(task_to_complete) - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == '5':
        # Organize tasks by priority
        tasks.sort(key=lambda x: x['priority'])
        print("Tasks organized by priority.")

    elif choice == '6':
        # Save tasks to the file before quitting
        save_tasks()
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
