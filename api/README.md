Task 0 - Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
REST API: https://jsonplaceholder.typicode.com/


Task 1 - Using what you did in the task #0, extend your Python script to export data in the CSV format.
Requirements:
Records all tasks that are owned by this employee, Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"


Task 2 - Using what you did in the task #0, extend your Python script to export data in the JSON format.
Requirements:
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}


Task 3 - Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:
Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}



