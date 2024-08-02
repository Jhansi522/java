# print the numbers that are divisible by both a and b from 20 to 100
a= int(input("Enter a:"))
b=int(input("Enter b:"))
b=4
res = []
for num in range(20,101):
    if num % a == 0 and num % b == 0:
        res.append(num)
print(res)