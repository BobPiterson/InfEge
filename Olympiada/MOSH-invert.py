f = open("D:/Users/bobpi/Downloads/e2.txt").read()[1:].split()

print(f[12])
output = []
for i in range(len(f)):
    output.append(f[i][::-1])
print()
print(output[12])
print(len(f[12]), len(output[12]))
