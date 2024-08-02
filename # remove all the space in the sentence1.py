# remove all the space in the sentence
s = "    this is python crt  "
res = ""
cnt = 0
for char in s:
    if char !=" ":
        res +=char
    else:
        cnt +=1
print(res)
print(cnt)
