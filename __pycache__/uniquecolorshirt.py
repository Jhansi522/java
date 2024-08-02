def unique(colors):
    unique_colors=set()
    for color in colors:
        unique_colors.add(color)
    return len(unique_colors)
n=int(input())
colors = list(map(int,input().split())
print(unique_colors)
