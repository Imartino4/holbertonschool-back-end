#!/usr/bin/python3
""" Request a RestAPI
    argv[1] -> user id
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    """ """

    u_id = int(argv[1])
    # APIS url
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    user = requests.get("https://jsonplaceholder.typicode.com/users")

    for u in user.json():
        if u["id"] == u_id:
            u_name = u["name"]
            break

    task_done = 0
    total_task = 0
    task_title = []
    for td in todo.json():
        if td["userId"] == u_id:
            total_task += 1
            if td["completed"]:
                task_done += 1
                task_title.append(td["title"])

    print("Employee {} is donde with tasks({}/{})".format(
                u_name, task_done, total_task))
    for title in task_title:
        print("\t {}".format(title))
