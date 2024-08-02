data = [
    # name  age salary id
    ("mahendra",23,50000,100),
    ("gautham",21,40000,101),
    ("hemanth",29,39000,102),
    ("upendra",30,50001,103)
]
 ###   
 # sort and print in alphabetical order
 #sort and print data in age order(younger's one's first)
  #sort and print data in age order(older's one's first)
  #print the older man name
  #print the younger ma name
  #print the richest employee name
   
#1
data.sort()
print(data)
#2
data.sort(key=lambda x:x[1])
print(data)
#3
data.sort(key=lambda x:x[1], reverse=True)
print(data)
#4
print(max(data, key=lambda x:x[1])[0])
#5
print(min(data, key=lambda x:x[1])[0])
#6
print(max(data, key=lambda x:x[2])[0])