n = int(input())
M = float(input())
t = float(input()) * 365 * 24 * 3600
k = float(input())
g = 9.81
T0 = 0
T = [0] * (n + 1)
for i in range(1, n + 1):
    T[i] = float(input()) * 7 * 24 * 3600
    T0 += T[i] / 2 ** i
R0 = k * g * T0 ** 2 / 2
r = k * g * T0 * t
R = [0] * (n + 1)
R[0] = R0
P = k * g * T0
for i in range(1, n + 1):
    Tdiff = 0  

if i == 1:
    Tdiff -= k * g * T[n] / 2 ** (n + 1)
else:
    for m in range(1, i):
        Tdiff -= k * g * T[m] / 2 ** m
    Tdiff -= k * g * T[i] / 2 ** (i + 1)
    R[i] = T[i] * (P + Tdiff)
R_ = (r + sum(R)) / (3e8 * 365 * 24 * 3600)
print(round(R_, 2)) 