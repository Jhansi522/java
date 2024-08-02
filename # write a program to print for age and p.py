# write a program to print for age and print if he is a kid/child/boy/old/man/immortal
age = int(input("Enter age:"))
if 1 <= age <= 5:
    print("He is kid")
elif 6 <= age <= 10:
    print("He is child")
elif 11 <= age <= 17:
    print("He is boy")
elif 18 <= age <= 59:
    print("He is man")
elif   60 <= age <= 100:
    print("He is old")
elif age > 100:
    print("Immortal")