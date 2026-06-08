import csv

from src.task import Task

def load_tasks(file_path):

    tasks = []

    with open(file_path) as file:

        reader = csv.DictReader(file)

        for row in reader:

            tasks.append(
                Task(
                    row["Task"],
                    int(row["Priority"]),
                    int(row["Deadline"]),
                    int(row["ExecutionTime"]),
                    int(row["Profit"])
                )
            )

    return tasks