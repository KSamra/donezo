from donezo.storage.storage import loadData

def get_tasks() -> dict:
    data = loadData()
    if not data:
        return {}

    return data['tasks']

def format(task: dict) -> str:
    return f"{task['id']} | {task['status']} | {task['description']}"



def filter_tasks(status: str | None, tasks: dict) -> list[str]:
    res = []
    if not tasks:
        return res

    if status:
        for key in tasks:
            if tasks[key]['status'] != status:
                continue
            else:
                res.append(format(tasks[key]))

    else:
        for key in tasks:
            res.append(format(tasks[key]))

    return res

def list_tasks(status: str | None = None) -> None:
    """
    Print tasks to console. Optionally filter tasks by status ('todo', 'in-progress', 'done')

    Returns:
        None
    """
    tasks = filter_tasks(status, get_tasks())
    if status:
        print(f"Total tasks with status of {status} = {len(tasks)}")
    else:
        print(f'Total tasks = {len(tasks)}')

    for task in tasks:
        print(task)
        


if __name__ == '__main__':
    list_tasks()
    
