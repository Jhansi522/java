import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

T = int(input())
for _ in range(T):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    d = set()
    d.add(distance(x1, y1, x2, y2))
    d.add(distance(x2, y2, x3, y3))
    d.add(distance(x3, y3, x4, y4))
    d.add(distance(x4, y4, x1, y1))
    d.add(distance(x1, y1, x3, y3))
    d.add(distance(x2, y2, x4, y4))
    if len(d) == 1:
        print("Yes")
    else:
        print("No")