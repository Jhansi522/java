a,b,c=list(map(int,input().split()))
if(a + b == c) or (a + c == b) or (b + c == a):
  print("Makes combination")
else:
 print("No combinations")