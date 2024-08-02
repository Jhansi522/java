# remove all the space in the sentence
s = "  this is python crt  "
res = ""
for char in s:
    if char !=" ":
        res +=char
print(res)