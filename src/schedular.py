import heapq

class Scheduler:

    def __init__(self, tasks):
        self.tasks = tasks

    def optimize_schedule(self):

        self.tasks.sort(key=lambda x: x.deadline)

        heap = []

        for task in self.tasks:
            heapq.heappush(
                heap,
                (-task.priority, task.deadline, task)
            )

        current_time = 0
        scheduled = []
        missed = []

        while heap:

            _, _, task = heapq.heappop(heap)

            if current_time + task.execution_time <= task.deadline:

                scheduled.append(task)
                current_time += task.execution_time

            else:

                missed.append(task)

        return scheduled, missed