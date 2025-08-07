from donezo.models.task import Task
from donezo.storage.storage import loadData, writeData

def add(desc: str) -> int:
    """
    Add a new task with the provided desc to be tracked

    Returns:
        int: the id of the newly created task
    """

    data = loadData()
    if not data:
        data = {}

    task_id = 0
    if data:
        task_id = data['latest_id']
        task_id += 1
        data['latest_id'] = task_id
        
    else:
        data['latest_id'] = task_id
        data['tasks'] = {}

    new_task = Task(task_id, desc)
    data['tasks'][str(task_id)] = new_task.to_dict()

    writeData(data)

    return task_id


if __name__ == '__main__':
    id = add('My first task!')
    print(f'created new task with {id=}')
    
