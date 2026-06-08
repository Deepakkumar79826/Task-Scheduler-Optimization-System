from src.task import Task
from src.validator import validate_task

task = Task(
    "Test",
    1,
    1,
    1,
    100
)

assert validate_task(task)