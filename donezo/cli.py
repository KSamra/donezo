import sys
import argparse
from commands import add_task, update_task, list_tasks, mark_task
# import os

def main():

    parser = argparse.ArgumentParser(prog='donezo', description='A simple task tracker')
    subparsers = parser.add_subparsers(dest='action', required=True)

    # Add command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('task_description', type=str)

    # Update command
    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('task_id', type=int)
    update_parser.add_argument('task_description', type=str)

    # Delete command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('task_id', type=int)
    

    #Mark-in-progress command
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress')
    mark_in_progress_parser.add_argument('task_id', type=int)

    #List command
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('task_status', type=str, choices=['done', 'todo', 'in-progress'])
    list_parser.add_argument('--value', type=lambda x: x.lower() == 'true', default=True, help='Boolean value to filter by. Default to TRUE')


    args = parser.parse_args()

    print(vars(args))
    
    if not args:
        sys.stderr.write('missing arguments to the cli')
        return

    match args.action:
        case 'add':
            task_desc = args.task_description
            # add(task_desc)
            new_task_id = add_task(task_desc)
        case 'update':
            task_id = args.task_id
            task_desc = args.task_description
            res = update_task(task_id, task_desc)
        case 'delete':
            task_id = args.task_id
        case 'mark-in-progress':
            task_id = args.task_id
            mark_task(task_id, 'in-progress')
        case 'mark-done':
            task_id = args.task_id
            mark_task(task_id, 'done')
        case 'list':
            task_status = args.task_status
            filter_value = args.value
            list_tasks(task_status, filter_value)
        case _:
            sys.stderr.write('invalid command supplied. See README')
            return

if __name__ == '__main__':
    main()
        
        