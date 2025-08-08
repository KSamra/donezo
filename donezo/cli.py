import sys
import argparse
# from .commands import add
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

    # Delete command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('task_id', type=int)
    

    #Mark-in-progress command
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress')
    mark_in_progress_parser.add_argument('task_id', type=int)

    #List command
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('task_status', type=str, choices=['done', 'todo', 'in-progress'])


    args = parser.parse_args()

    print(vars(args))
    
    if not args:
        sys.stderr.write('missing arguments to the cli')
        return

    match args.action:
        case 'add':
            task_desc = args.task_description
            print(f'running add with a task {task_desc=}')
            # add(task_desc)

        case 'update':
            task_id = args.task_id
            print(f'running update on {task_id=}')
        case 'delete':
            task_id = args.task_id
            print(f'running delete on {task_id=}')
        case 'mark-in-progress':
            task_id = args.task_id
            print(f'running mark-in-progress on {task_id=}')
        case 'mark-done':
            task_id = args.task_id
            print(f'runnning mark-done on {task_id=}')
        case 'list':
            task_status = args.task_status
            print(f'running list for all where {task_status=}')
        case _:
            sys.stderr.write('invalid command supplied. See README')
            return

if __name__ == '__main__':
    main()
        
        