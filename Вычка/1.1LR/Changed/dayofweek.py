import sys

y = int(sys.argv[1])
m = int(sys.argv[2])
d = int(sys.argv[3])

y1 = y - (14 - m) // 12

x = y1 + y1 // 4 - y1 // 100 + y1 // 400

m1 = m + 12 * ((14 - m) // 12) - 2

d1 = (d + x + 31 * m1 // 12) % 7

print(str(d1))