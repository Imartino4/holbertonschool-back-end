#!/usr/bin/python3
""" Request a RestAPI and export to CSV file
    argv[1] -> user id
    CSV filename must be <user_id>.csv
"""
import csv
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
            u_username = u["username"]
            break

    file_name = "{}.csv".format(u_id)
    with open(file_name, 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for td in todo.json():
            if td["userId"] == u_id:
                task_status = td["completed"]
                task_title = td["title"]
                writer.writerow([u_id, u_username, task_status, task_title])
