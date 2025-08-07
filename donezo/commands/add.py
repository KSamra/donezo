from donezo.models.task import Task
from donezo.storage import getDataPath
import json

def add(desc: str) -> int:
    """
    Add a new task with the provided desc to be tracked

    Returns:
        int: the id of the newly created task
    """
    data_path = getDataPath()

    try:
        with open(data_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    task_id = 0
    if data:
        task_id = data['latest_id']
        task_id += 1
        data['latest_id'] = task_id
        
    else:
        data['latest_id'] = task_id

    new_task = Task(task_id, desc)
    data['tasks'][str(task_id)] = new_task.to_dict()

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    return task_id


if __name__ == '__main__':
    id = add('My first task!')
    print(f'created new task with {id=}')
    
