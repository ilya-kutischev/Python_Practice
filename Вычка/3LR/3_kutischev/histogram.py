import sys
filename = sys.argv[1]
amount = int(sys.argv[2])
data = []
with open(filename) as f:
    for line in f:
        data += [float(x) for x in line.split()]
minimal = min(data)
maximal = max(data)
delta = (maximal - minimal) / amount
normal = []
for i in range(amount):
    normal.append(0)
    for num in data:
        if num >= minimal + delta * i and num <= minimal + delta * (i + 1):
            normal[i] += 1
print(normal)


