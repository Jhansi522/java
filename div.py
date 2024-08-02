a,b,c=map(int,input().split())
cnt = 0
if a % b == 0:
    cnt +=1
if a % c == 0:
    cnt +=1
if b % a == 0:
    cnt +=1
if b % c == 0:
    cnt +=1
if c % a == 0:
    cnt +=1
if c % b == 0:
    cnt +=1
print(cnt)