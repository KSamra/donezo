import datetime
class Task:
    def __init__(self, id: int, desc: str):
        self.id = id
        self.description = desc
        self.status = 'todo'
        self.createdAt = datetime.datetime.now(datetime.timezone.utc)
        self.updatedAt: datetime.datetime | None = None

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None
        }
    
if __name__ == '__main__':

    #testing Task serialization/deserialization
    test_task = Task(0, 'testing')

    #json serialization
    task_dict = test_task.to_dict()
    print(f'{task_dict=}')
    import json
    task_json = json.dumps(task_dict)
    print(f'{task_json=}')

    #json deserialization
    print('deserializing')
    task_dict = json.loads(task_json)
    print(f'{task_dict=}')
    