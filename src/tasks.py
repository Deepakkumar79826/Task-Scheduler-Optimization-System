from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: int
    deadline: int
    execution_time: int
    profit: int