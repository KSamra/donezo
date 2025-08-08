from donezo.models.task import Task
from donezo.storage.storage import loadData, writeData

def update_task(id: int, desc: str) -> bool:
    """
    Update a task with the provided id. Overwrites the existing task description to what is provided in desc

    Returns:
        bool: whether the task was updated or not. If False, the task does not exist
    """

    data = loadData()
    if not data:
        print('Tried to update but there is no data to update')
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

        writeData(data)

    else:
        print(f'There is no task with {id=} being tracked')
        return False
    
    return True

if __name__ == '__main__':
    
    res = update_task(3, 'super cool update')
    print(f'update result = {res}')