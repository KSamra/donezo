import os
import json

# %%
def getDataPath() -> str:
    """
    The .json file path where user tasks are stored

    Returns:
        str: the full path of the storage.json file location
    """

    home_dir = os.path.expanduser('~')
    data_dir = os.path.join(home_dir, '.donezo')
    os.makedirs(data_dir, exist_ok=True)
    data_path = os.path.join(data_dir, 'data.json')
    return data_path

def loadData() -> dict | None:
    """
    Load data from .json storage file. 

    Returns:
        dict | None: User data in the form of a dictionary in json format (all keys are strings), or None
    """
    path = getDataPath()

    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print('Data file not found!')
        return None
    except json.JSONDecodeError:
        print('Data file is corrupted or improperly formatted.')
        return None
    
    return data

def writeData(data: dict) -> None:
    """
    Write the provided data to storage. 'data' must be a dictionary who's keys adhere to json formatted (keys are strings)

    Returns:
        None
    """
    path = getDataPath()

    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
    except TypeError as e:
        print('Writing to storage failed: ', e)



def printStorage() -> None:
    """
    print output of storage file to console

    Returns:
        None
    """
    path = getDataPath()

    try:
        with open(path, 'r') as f:
            for line in f.readlines():
                print(line)
    except FileNotFoundError:
        print('File does not exist!')

if __name__ == '__main__':
    path = getDataPath()
    print(f'Storage file_path = {path}')
    printStorage()



