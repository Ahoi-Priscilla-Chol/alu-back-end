#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file using a REST API."""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get(base_url + "/users/" + user_id).json()
    todos = requests.get(base_url + "/todos",
                         params={"userId": user_id}).json()

    tasks = [{"task": t.get("title"),
              "completed": t.get("completed"),
              "username": user.get("username")} for t in todos]

    with open(user_id + ".json", "w") as file:
        json.dump({user_id: tasks}, file)
