import sys
st = sys.argv[1]
left=0
right = 0
for i in range(len(st)):
    if st[i] == "(":
        left += 1
    if st[i] == ")":
        right += 1

print(left == right)