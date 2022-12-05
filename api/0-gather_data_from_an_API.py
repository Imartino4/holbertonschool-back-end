#!/usr/bin/python3
""" Request a RestAPI
    argv[1] -> user id
"""
import requests
from sys import argv


if __name__ == '__main__':
    """ """

    u_id = int(argv[1])
    # APIS url, se podrian pedir solo las correspondiemtes al id
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get("https://jsonplaceholder.typicode.com/users").json()

    for u in user:
        if u["id"] == u_id:
            u_name = u["name"]
            break

    task_title = []
    total_task = 0
    for td in todo:
        if td["userId"] == u_id:
            total_task += 1
            if td["completed"]:
                task_title.append(td["title"])

    print("Employee {} is donde with tasks({}/{})".format(
                u_name, len(task_title), total_task))
    for title in task_title:
        print("\t {}".format(title))
