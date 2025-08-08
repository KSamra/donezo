from donezo.storage import loadData, writeData

def delete_task(task_id: int) -> bool:
    
    data = loadData()

    if not data:
        return False
    
    tasks = data['tasks']
    str_id = str(task_id)
    if str_id not in tasks:
        return False

    del tasks[str_id]
    
    writeData(data)
    return True
    


if __name__ == '__main__':
    delete_task(5) 