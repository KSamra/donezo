from donezo.models.task import Task
from donezo.storage import getDataPath
import json

def add(desc: str):
    data_path = getDataPath()

    try:
        with open(data_path, "r") as f:
            data = json.load(f)
            print(f'{data=}')
    except FileNotFoundError:
        data = {}


    if data:
        task_id = data['latest_id']
        task_id += 1
        data['latest_id'] = task_id
        new_task = Task(task_id, desc)
        data['tasks'].append(new_task.to_dict())

    else:
        data['latest_id'] = 0
        new_task = Task(0, desc)
        data['tasks'] = []
        data['tasks'].append(new_task.to_dict())

    
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    add('My first task!')
