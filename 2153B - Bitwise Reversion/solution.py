import sys

input = sys.stdin.read
data = input().split()
iterator = iter(data)

t = int(next(iterator))
results = []

for _ in range(t):
    x = int(next(iterator))
    y = int(next(iterator))
    z = int(next(iterator))

    if ((x & y) & ~z) | ((x & z) & ~y) | ((y & z) & ~x):
        results.append("NO")
    else:
        results.append("YES")

print('\n'.join(results))