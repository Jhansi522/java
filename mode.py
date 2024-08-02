# mode of 2,2,4,2,8,6,7
arr = [2,2,4,2,8,6,7]
counter = {}
counter[2] = arr.count(2)
for num in arr: #to count &store the frequencies
    counter[num] = arr.count(num)
max_repeated_cnt = max(counter.values()) # to get highest request count
for num in counter:
    if counter[num] == max_repeated_cnt:
        print("Mode of {arr} is {num}")
print(counter)