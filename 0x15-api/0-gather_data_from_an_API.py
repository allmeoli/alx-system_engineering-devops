#!/usr/bin/python3

import requests
from sys import argv

if __name__ == "__main__":

    url_user = "https://jsonplaceholder.typicode.com/users/{}/".format(argv[1])
    url_user_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
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
    print('Employee {0} is done with tasks({1}/{2}):'.format(name,
          total_num_cmp, total_num_oftask))
    for task in tasks_completed:
        print("\t {}".format(task))
