import csv

processes = {'0': [0, ['0'], 0]}
with open('22 (3).csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        if row[0].isnumeric():
            processes[row[0]] = [int(row[1]), row[2].split(';'), 0]

for i in range(10):
    for idx, data in processes.items():
        time, deps, _ = data
        processes[idx][2] = max(processes[dep][2] for dep in deps) + time

results = list(map(lambda a: a[2], processes.values()))
results.sort()
print(results[70])
