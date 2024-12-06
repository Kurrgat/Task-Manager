# tasks = []

# def add_task(task):
#     tasks.append(task)
#     print(f'Task added: {task}')

import json

# Path to the tasks JSON file (or database setup)
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(name, description):
    """Add a new task."""
    tasks = load_tasks()
    new_task = {"name": name, "description": description}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{name}' added successfully!")

if __name__ == "__main__":
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    add_task(task_name, task_description)

