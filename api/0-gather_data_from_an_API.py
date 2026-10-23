#!/usr/bin/python3
"""Gather employee TODO list progress from a REST API."""

import json
import sys
from urllib.request import urlopen


def main():
    """Display an employee's completed TODO tasks."""
    employee_id = int(sys.argv[1])

    with urlopen(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id
        )
    ) as response:
        employee = json.loads(response.read().decode("utf-8"))

    with urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    ) as response:
        todos = json.loads(response.read().decode("utf-8"))

    completed_tasks = [
        task for task in todos
        if task.get("completed")
    ]

    employee_name = employee.get("name")
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_count, total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
