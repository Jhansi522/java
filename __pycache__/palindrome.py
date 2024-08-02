#METHOD-1
#def isPalindrome(self, x: int) -> bool:
#    if x<0:
       #return False
    #r=0
        #temp = x
        #while temp>0:
         #   digit=temp%10
          #  r=r*10+digit
           # temp//=10
        #return r == x  



















#METHOD-2
#def isPalindrome(s):
 #   return s == s[::-1]


#s = "malayalam"
#ans = isPalindrome(s)
#if ans:
 #   print("Yes")
#else:
 #   print("No")



#METHOD-3
def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False


s =input()
ans = isPalindrome(s)
if (ans):
    print("IT IS A PALINDROME")
else:
    print("IT IS NOT PALINDROME")
