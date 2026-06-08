from src.utils import load_tasks
from src.scheduler import Scheduler

tasks = load_tasks("data/tasks.csv")

scheduler = Scheduler(tasks)

scheduled, missed = (
    scheduler.optimize_schedule()
)

assert len(scheduled) > 0