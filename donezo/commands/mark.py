from donezo.storage.storage import loadData, writeData

def mark_task(id: int, status: str) -> bool:
    """
    Update the task with the given 'id' with the provided 'status'

    Returns:
        bool: If the update occurred, or not. If the task does not exist then this is also False
    """
    statuses = ['todo','done', 'in-progress']

    if status and status not in statuses:
        print(f"Provided {status=} is not allowed. Choose either 'todo', 'done' or 'in-progress' ")
        return False
    data = loadData()
    if not data:
        return False
    
    tasks = data['tasks']
    if str(id) in tasks:
        task = tasks[str(id)]
        task['status'] = status
        writeData(data)
    else:
        print(f"Task with {id=} does not exist. Cannot update")
        return False


    return True


if __name__ == '__main__':
    res = mark_task(0, 'done')
    res2 = mark_task(1, 'in-progress')
    