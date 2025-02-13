print("Task Tracker Initialized")
def list_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")