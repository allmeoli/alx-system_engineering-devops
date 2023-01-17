#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":

    url_user = "https://jsonplaceholder.typicode.com/users/{}/"\
        .format(argv[1])
    url_user_todo = "https://jsonplaceholder.typicode.com/users/{}/todos"\
        .format(
            argv[1])

    res_user = requests.get(url_user)
    res_user_todo = requests.get(url_user_todo)

    name = res_user.json()["name"]
    total_num_oftask = len(res_user_todo.json())
    total_num_cmp = 0
    tasks_completed = []
    for x in res_user_todo.json():
        if x['completed']:
            total_num_cmp += 1
            tasks_completed.append(x['title'])
    print('Employee {} is done with tasks({}/{}):'.format(name,
          total_num_cmp, total_num_oftask))
    for task in tasks_completed:
        print("\t {}".format(task))
