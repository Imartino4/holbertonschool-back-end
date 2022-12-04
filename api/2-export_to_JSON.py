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

    list_of_dict = []
    todo_dict = {}
    for td in todo.json():
        if td['userId'] == u_id:
            todo_dict['task'] = td['title']
            todo_dict['completed'] = td['completed']
            todo_dict['username'] = u_username
            list_of_dict.append(todo_dict)
    json_dict = {}
    json_dict[u_id] = list_of_dict

    file_name = "{}.json".format(u_id)
    with open(file_name, 'w') as f:
        f.write(json.dumps(json_dict))
