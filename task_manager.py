import json

class Task:
    def __init__(self, id, name, description, completed=False):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else " "
        return f"Task: {self.name}\nDescription: {self.description}\nStatus: {status}"


class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load_tasks()

    def add_task(self, name, description):
        task = Task(self.next_id, name, description)
        self.tasks.append(task)
        self.next_id += 1   
        self.save_tasks()
        print(f"Task '{name}' added successfully.")

    def list_tasks(self):
        if not self.tasks:
            return "No tasks available."
        else:
            for task in self.tasks:
                print(task)

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_completed()
                return f"Task '{name}' marked as completed."
        return f"Task '{name}' not found."
    
    def delete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                return f"Task '{name}' has been deleted."
        return f"Task '{name}' not found."
    

    def load_tasks(self, filename=FILENAME):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.tasks = [Task(**task) for task in data.get("tasks", [])]
                self.next_id = data.get("next_id", 1)
        except FileNotFoundError:
            print("No existing tasks found. Starting with an empty task list.")
        except json.JSONDecodeError:
            print("Error loading tasks. Starting with an empty task list.")
    
    def save_tasks(self, filename=FILENAME):
         with open(filename, 'w') as file:
             data = {
                 "tasks": [task.__dict__ for task in self.tasks],
                 "next_id": self.next_id
             }
             json.dump(data, file, indent=4)