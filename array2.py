arr = [1,2,5,0,12,8,0,7,0]
temp = []
zero_cnt = 0
for num in arr:
    if num !=0:
        temp.append(num)
    else:
        zero_cnt +=1
print(temp, zero_cnt)