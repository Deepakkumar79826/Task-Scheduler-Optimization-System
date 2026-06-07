import heapq
import csv
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: int
    deadline: int
    execution_time: int
    profit: int

tasks = [
    Task("Assignment",5,2,1,100),
    Task("Project",4,4,2,200),
    Task("Presentation",8,1,1,150),
    Task("Coding Practice",3,3,1,80),
    Task("Research",6,2,1,120)
]

tasks.sort(key=lambda x: x.deadline)

heap = []
current_time = 0
scheduled = []
missed = []

for task in tasks:
    heapq.heappush(heap, (-task.priority, task.deadline, task))

while heap:
    _, _, task = heapq.heappop(heap)
    if current_time + task.execution_time <= task.deadline:
        scheduled.append(task)
        current_time += task.execution_time
    else:
        missed.append(task)

profit = sum(t.profit for t in scheduled)

print("\nOPTIMIZED SCHEDULE\n")

timeline = []
start = 0

for task in scheduled:
    end = start + task.execution_time
    timeline.append([task.name, start, end])
    print(f"{task.name} ({start}-{end})")
    start = end

print("\nMISSED TASKS")
for task in missed:
    print(task.name)

print("\nTOTAL PROFIT:", profit)

with open("schedule_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Task", "Start", "End"])
    writer.writerows(timeline)

print("\nCSV Report Generated")
