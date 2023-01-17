#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('name')

    id = sys.argv[1]
    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    l_task = []

    name_first = name.split(" ")[0]
    with open('{}.json'.format(id), 'w', encoding='UTF8') as f:
        for task in tasks:
            dictionary = {
                "task": task.get('title'), "completed":
                    task.get('completed'), "username":
                name_first}
            l_task.append(dictionary)
        dicr = {id: l_task}
        json.dump(dicr, f, ensure_ascii=True)
