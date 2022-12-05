#!/usr/bin/python3
""" Request a RestAPI and export to JSON file
"""
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    """ """

    # APIS url
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(user_url)
    todo = requests.get(todo_url)

    json_dict = {}
    for u in user.json():
        list_of_dict = []
        u_username = u['username']
        u_id = u['id']
        for td in todo.json():
            if u_id == td['userId']:
                todo_dict = {}
                todo_dict['username'] = u_username
                todo_dict['task'] = td['title']
                todo_dict['completed'] = td['completed']
                list_of_dict.append(todo_dict)
            json_dict[u_id] = list_of_dict

    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as f:
        f.write(json.dumps(json_dict))
