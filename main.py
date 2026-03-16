import task_manager

def main():
    manager = task_manager.TaskManager()
    while True:

        print("\n---- Welcome to the Task Manager ----\n")
        print("Available commands:")
        print("1. add - Add a new task")
        print("2. list - List all tasks")
        print("3. complete - Mark a task as completed")
        print("4. delete - Delete a task")
        print("5. exit - Exit the application\n")

        choice = input("Enter your choice: ").strip().lower()
        match choice:
            case "1" :
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                manager.add_task(name, description)
                print(f"Task '{name}' added successfully.")
            case "2" :
                 print(manager.list_tasks())
            case "3" :
                name = input("Enter task name to mark as completed: ")
                print(manager.complete_task(name))
            case "4" :
                name = input("Enter task name to delete: ")
                print(manager.delete_task(name))
            case "5" :
                print("Exiting the Task Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()