n= 6
arr = [1,2,3,4,5,6]
mid = n//2
sub1 = arr[:mid]
sub2 = arr[mid:][::-1]
res = []
for i in range(n//2):
    res.append(sub1[i])
    res.append(sub2[i])
print(res)
# for odd length condition
if n % 2 !=0:
    res.append(arr[mid])
print(res)