import datetime
class Task:
    def __init__(self, id: int, desc: str):
        self.id = id
        self.description = desc
        self.status = 'todo'
        self.createdAt = datetime.datetime.now(datetime.timezone.utc)
        self.updatedAt: datetime.datetime | None = None

    def update_description(self, desc: str):
        self.description = desc
        self.updatedAt = datetime.datetime.now(datetime.timezone.utc)

    #remember the update time as well
    def update_status(self, status: str):
        pass

    def to_dict(self) -> dict:
        """
        Serialize self into a json formatted dictionary

        Returns:
            dict: json formatted dictionary representing the object
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """
        Initialize and return a Task object using the provided json-formatted dictionary
        """
        task = cls(int(data['id']), data['description'])
        task.status = data['status']
        task.createdAt = datetime.datetime.fromisoformat(data['createdAt'])
        updated_at = data['updatedAt']
        task.updatedAt = datetime.datetime.fromisoformat(updated_at) if updated_at else None

        return task

        

    
if __name__ == '__main__':

    #testing Task serialization/deserialization
    test_task = Task(0, 'testing')

    #json serialization
    task_dict = test_task.to_dict()
    print('serializing to dict')
    print(f'{task_dict=}')
    import json
    task_json = json.dumps(task_dict)
    print('writing to json')
    print(f'{task_json=}')

    # #json deserialization
    print('deserializing back into Task')
    task_dict = json.loads(task_json)
    t = Task.from_dict(task_dict)
    
    