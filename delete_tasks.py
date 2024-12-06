import json

# Path to the tasks JSON file
TASKS_FILE = "tasks_data.json"

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

def delete_task(name):
    """Delete a task by name."""
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['name'] != name]
    if len(tasks) == len(updated_tasks):
        print(f"Task '{name}' not found!")
    else:
        save_tasks(updated_tasks)
        print(f"Task '{name}' deleted successfully!")

if __name__ == "__main__":
    task_name = input("Enter the name of the task to delete: ")
    delete_task(task_name)
