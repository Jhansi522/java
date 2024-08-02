arr = [1,2,3,2,4]
#apporach 2
#print(len(arr) != len(set(arr))) #edi test cases lo pass avuthamuu
#approach 1
validated = set()
for num in arr:
    if num in validated:
        print("True")
        break
    validated.add(num)
else:
    print("False")
