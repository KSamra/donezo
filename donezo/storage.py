import os

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


if __name__ == '__main__':
    path = getDataPath()
    print(f'received file_path = {path}')


