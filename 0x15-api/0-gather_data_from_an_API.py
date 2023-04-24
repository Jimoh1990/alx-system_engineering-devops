#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    response = requests.get(url)
    user = response.json()
    name = user.get('name')

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        sys.argv[1])
    response = requests.get(url)
    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]
    completed_count = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        name, completed_count, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

