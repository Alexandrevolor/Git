print("Task Tracker Initialized")
<<<<<<< HEAD
def add_task(tasks, task):
    tasks.append(task)
    print(f"Task added: {task}")

def list_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")