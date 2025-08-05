import sys
import argparse
from .commands import add
import os

def main():

    home_dir = os.path.expanduser('~')
    data_dir = os.path.join(home_dir, '.donezo')
    os.makedirs(data_dir, exist_ok=True)
    data_path = os.path.join(data_dir, 'data.json')

    print(f'Storing tasks in {data_path}')

    parser = argparse.ArgumentParser(prog='donezo', description='A simple task tracker')
    subparsers = parser.add_subparsers(dest='action', required=True)

    # Add command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('task_description', type=str)

    # Update command
    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('task_id', type=int)

    # Delete command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('task_id', type=int)
    args = parser.parse_args()

    
    if not args:
        sys.stderr.write('missing arguments to the cli')
        return

    match args.action:
        case 'add':
            task_desc = args.task_description
            add(task_desc)

        case 'update':
            print('running update')
        case 'delete':
            print('running delete')
        case 'mark-in-progress':
            print('running mark-in-progress')
        case 'mark-done':
            print('runnning mark-done')
        case 'list':
            print('running list')
        case _:
            sys.stderr.write('invalid command supplied. See README')
            return
        
        