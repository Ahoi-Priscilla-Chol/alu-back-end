#!/usr/bin/python3
"""Export all employees' TODO lists to one JSON file using a REST API."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get(base_url + "/users").json()
    todos = requests.get(base_url + "/todos").json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        all_tasks[str(user_id)] = [
            {"username": user.get("username"),
             "task": t.get("title"),
             "completed": t.get("completed")}
            for t in todos if t.get("userId") == user_id]

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_tasks, file)
