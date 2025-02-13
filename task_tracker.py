print("Task Tracker Initialized")
<<<<<<< HEAD
def add_task(tasks, task):
    tasks.append(task)
    print(f"Task added: {task}")

def list_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def remove_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number")