# median of 2,1,4,10,8,6,7
arr = [2,1,4,10,8,6,7]
arr.sort()
mid = len(arr) // 2
if len(arr) % 2 == 0:
    print(f"Median of(arr) is {(arr[mid] + arr[mid-1])//2}")
else:
    print("Median of {arr} is {arr[mid]}")