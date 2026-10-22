#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file using a REST API."""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get(base_url + "/users/" + user_id).json()
    todos = requests.get(base_url + "/todos",
                         params={"userId": user_id}).json()

    with open(user_id + ".csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, lineterminator="\n")
        for t in todos:
            writer.writerow([user_id, user.get("username"),
                             t.get("completed"), t.get("title")])
