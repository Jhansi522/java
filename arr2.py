arr = [1,2,3,2,4,4]

#approach 1
validated = set()
res = []
for num in arr:
    if num in validated:
        res.append(num)
        #break
    validated.add(num)
if len(res) != 0:
    print(res)
else:
    print("No duplicates")

