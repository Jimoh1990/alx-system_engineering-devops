#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress and exports it to a CSV file.
"""
import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    response = requests.get(url)
    user = response.json()
    username = user.get('username')
    user_id = user.get('id')

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        sys.argv[1])
    response = requests.get(url)
    todos = response.json()

    with open('{}.csv'.format(user_id), mode='w') as csv_file:
        writer = csv.writer(
            csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            completed = todo.get('completed')
            title = todo.get('title')
            writer.writerow([user_id, username, completed, title])
