#!/usr/bin/python3
""" Request a RestAPI """
import json
import requests
from sys import argv


if __name__ == '__main__':
    """ """

    u_id = int(argv[1])
    # APIS url
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(user_url)
    todo = requests.get(todo_url)

    for u in user.json():
        if u["id"] == u_id:
            u_name = u["name"]
            break

    total_task = 0
    task_title = []
    for td in todo.json():
        if td["userId"] == u_id:
            total_task += 1
            if td["completed"]:
                task_title.append(td["title"])

    print("Employee {} is donde with tasks({}/{}):".format(
                u_name, len(task_title), total_task))
    for title in task_title:
        print("\t {}".format(title))
