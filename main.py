from ai_service import create_simple_task
import task_manager

def main():
    manager = task_manager.TaskManager()
    while True:

        print("\n---- Welcome to the Task Manager ----\n")
        print("Available commands:")
        print("1. add - Add a new task")
        print("2. add IA - Add a new task using AI")
        print("3. list - List all tasks")
        print("4. complete - Mark a task as completed")
        print("5. delete - Delete a task")
        print("6. exit - Exit the application\n")
        choice = input("Enter your choice: ").strip().lower()
        match choice:
            case "1" :
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                manager.add_task(name, description)
                print(f"Task '{name}' added successfully.")
            case "2" :
                description = input("Enter task description: ")
                subtasks = create_simple_task(description)
                print(f"Task added successfully with AI-generated subtasks:")
                for i, subtask in enumerate(subtasks, 1):
                    print(f"{i}. {subtask}")
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