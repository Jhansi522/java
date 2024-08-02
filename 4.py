#get all palindrome numbers from 1 to 200
print([num for num in range(1,201)if str(num) == str(num)[::-1]])
