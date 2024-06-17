with open('inputs/09.txt', 'r') as file:
    lines = [sorted((map(int, line.split()))) for line in file.readlines()]

print(lines)
cnt = sum(1 for a, b, c in lines if a * a + b * b == c * c)
print(cnt)
