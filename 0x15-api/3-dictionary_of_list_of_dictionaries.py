#!/usr/bin/python3
"""Extend script to export data in the JSON format."""

import json
import requests
from sys import argv

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    users_req = requests.get("{}/users".format(api_url)).json()
    tasks_dict = {}
    for user in users_req:
        tasks_req = requests.get("{}/todos?userId={}".format(api_url,
                                                      user.get("id")
                                                      )).json()
        tasks_list = []
        for task in tasks_req:
            task_dict = {"username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")}
            tasks_list.append(task_dict)
        tasks_dict[user.get("id")] = tasks_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(tasks_dict, f)                              
