# join the list elements into single string
words = ["this", "is", "pen"]
res = ""
for w in words:
    res = res +str(w)
    res = res + "-"
print(res[:-1])
