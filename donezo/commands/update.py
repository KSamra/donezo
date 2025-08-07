from donezo.models.task import Task
from donezo.storage import getDataPath
import json

def update(id: int, desc: str) -> bool:
    """
    Update a task with the provided id. Overwrites the existing task description to what is provided in desc

    Returns:
        bool: whether the task was updated or not. If False, the task does not exist
    """
    #see if the task exists
    path = getDataPath()
    
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f'There is no storage file to update')
        return False
    
    tasks = data['tasks']
    str_id = str(id)
    if str_id in tasks:
        #convert to Task object and update description
        task = Task.from_dict(tasks[str_id])
        task.update_description(desc)

        #convert Task back to json formatted dictionary
        task_dict = task.to_dict()

        #write back to storage
        tasks[str_id] = task_dict
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    else:
        print(f'There is no task with {id=} being tracked')
        return False
    
    return True

if __name__ == '__main__':
    
    res = update(1, 'nothing')
    print(f'update result = {res}')