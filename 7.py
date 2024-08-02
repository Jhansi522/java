def isComposites(n):
    for i in range(2,(n//2)+1):
        if n % i == 0:
            return False
    return True
for n in [9,31,32,14,17,43,58,5,6]:
   if isComposites(n) == True:
    print(n)
