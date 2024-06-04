from typing import List, Dict


class Process:
    def __init__(self, idx: str, time: int, deps: List[str]):
        self.idx = idx
        self.time = time
        if deps[0] == '0':
            self.deps = None
        else:
            self.deps = deps

    def __str__(self):
        return f'{self.time} {self.deps}'


processes: Dict[str, Process] = {}
with open('inputs/22.txt', 'r') as file:
    for line in file:
        idx, time, deps = line.split()
        time = int(time)
        deps = deps.split(';')
        processes[idx] = Process(idx, time, deps)

end: Dict[str, int] = {idx: 0 for idx in processes.keys()}
for i in range(1000):
    for process in processes.values():
        if process.deps:
            end[process.idx] = max(end[dep] for dep in process.deps) + process.time
        else:
            end[process.idx] = process.time

sr = sorted(end, key=lambda x: end[x])
print(end[sr[69]])
