import math

g = 9.81
c = 3 * 10 ** 8
n = int(input())
M = float(input()) * 1000
t = float(input())
k = float(input()) 

t = t * 365 * 24 * 60 * 60
times = []
for i in range(n):
    times.append(float(input()) * 7 * 24 * 60 * 60)

d = 0
v = 0

a = k * g
d += a * (times[0] ** 2) / 2
v += a * times[0]

d += t * v

for idx, time in enumerate(times[1:]):
    a = (k * g) / (2 ** (idx + 1))
    d += v * time - a * time ** 2 / 2
    v -= a * time

d = d / c / 60 / 60 / 24 / 365
print(round(d, 2))