#!/usr/bin/python3
"""
Using the JSONPlaceholder API, export data in the JSON format.

Records all tasks that are owned by this employee
Format must be: {"USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = base_url + "/users/" + user_id
    todo_url = base_url + "/todos?userId=" + user_id

    # get user information
    user_info = requests.get(user_url).json()
    user_name = user_info.get("username")

    # get user's to-do list
    todo_list = requests.get(todo_url).json()

    # create dictionary to hold user's to-do list
    todo_dict = {}
    todo_dict[user_id] = []

    # fill in the dictionary with relevant information
    for todo in todo_list:
        task_dict = {}
        task_dict["task"] = todo.get("title")
        task_dict["completed"] = todo.get("completed")
        task_dict["username"] = user_name
        todo_dict[user_id].append(task_dict)

        # write data to JSON file
        filename = user_id + ".json"
        with open(filename, mode="w") as file:
            json.dump(todo_dict, file)
