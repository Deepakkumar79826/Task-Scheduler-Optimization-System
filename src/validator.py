def validate_task(task):
    if task.priority <= 0:
        return False

    if task.deadline <= 0:
        return False

    if task.execution_time <= 0:
        return False

    if task.profit < 0:
        return False

    return True