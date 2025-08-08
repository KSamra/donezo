from donezo.storage.storage import loadData

def get_tasks() -> dict:
    data = loadData()
    if not data:
        return {}

    return data['tasks']

def format(task: dict) -> str:
    #<3 and <12 means 'left-align in field with this many characters. [:30] means limit to 30 characters
    return f"{task['id']: <3} | {task['status']: <12} | {task['description'][:30]}"

def header() -> str:
    return f"{'ID': <3} | {'Status': <12} | {'Description': <30}"



def filter_tasks(status: str | None, tasks: dict, match_status: bool = True) -> list[str]:
    res = []
    if not tasks:
        return res

    if status:
        for key in tasks:
            if (tasks[key]['status'] == status and match_status) or (tasks[key]['status'] != status and not match_status):
                res.append(format(tasks[key]))
    else:
        for key in tasks:
            res.append(format(tasks[key]))

    return res

def list_tasks(status: str | None = None, match_status: bool = True) -> None:
    """
    Print tasks to console. Optionally filter tasks by status ('todo', 'in-progress', 'done') with the option
    to match against that status or not. Ex, 'status'='done', 'match_status'=False would then return all tasks where 'status' is NOT 'done'

    Params:
        status: the status we want to match with,
        match_status: optionally, if we want to match with or against the provided status. Example, i

    Returns:
        None
    """
    
    tasks = filter_tasks(status, get_tasks(), match_status)
    if status:
        print(f"{len(tasks)} total tasks where '{status}' = '{match_status}'")
    else:
        print(f'Total tasks = {len(tasks)}')

    print(header())
    for task in tasks:
        print(task)
        


if __name__ == '__main__':
    # list_tasks('in-progress')
    list_tasks()
    
