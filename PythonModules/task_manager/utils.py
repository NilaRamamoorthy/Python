def generate_task_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1
