# num = int(input())
# rev = 0
# while(num != 0):
#      curr_rev = num%10
#      num = num//10
#      rev = rev*10 + curr_rev

# num1 = int(input())
# if(rev == num1):
#      print("true")
# else:
#      print("false")

def checkPalindrome(num):
    rev = 0
    while(num != 0):
        curr_rev = num%10
        num = num//10
        rev = rev*10 + curr_rev
        pass
		
num = int(input())
rev = num
if(rev):
 	print('true')
else:
 	print('false')

